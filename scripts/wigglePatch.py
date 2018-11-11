#!/usr/bin/env python3
from subprocess import run, PIPE, CalledProcessError
from argparse import ArgumentParser
import os
from os import path
from sys import stderr, stdout
import re
from enum import Enum, unique

@unique
class FileStatus(Enum):
    UNTRACKED = '?'
    UNMODIFIED = ' '
    MODIFIED = 'M'
    ADDED = 'A'
    DELETED = 'D'
    RENAMED = 'R'
    COPIED = 'C'
    UNMERGED = 'U'
    IGNORED = '!'

class GitRepository:
    def __init__(self, directory):
        if not path.isdir(directory):
            if not path.exists(directory):
                raise ValueError("Repository doesn't exist:", directory)
            else:
                raise ValueError("Repository isn't a valid directory:", directory)
        elif not path.isdir(path.join(directory, ".git")):
            raise ValueError("Directory isn't a git repository:", directory)
        self.directory = directory

    def status(self):
        status_lines = run(
            ["git", "status", "--porcelain"],
            check=True, stdout=PIPE, universal_newlines=True,
            cwd=self.directory
        ).stdout
        status = dict()
        for line in status_lines.splitlines():
            old_status = FileStatus(line[0])
            new_status = FileStatus(line[1])
            file_name = line[3:]
            status[file_name] = (old_status, new_status)
        return status

    def is_clean(self):
        try:
            return len(self.status()) == 0
        except CalledProcessError:
            return False

    def is_automatically_merging(self):
        return path.exists(path.join(self.directory, ".git", "rebase-apply", "applying"))

    def wiggle_patch(self, patch):
        assert self.is_clean()
        # By default, wiggle won't create files the patch needs, and just fails
        for created_file in patch.created_files:
            # mkdir -p $(dirname created_file)
            os.makedirs(path.join(self.directory, path.dirname(created_file)), exist_ok=True)
            # touch created_file
            with open(path.join(self.directory, created_file), 'a'):
                pass
        result = run(["wiggle", "-rp", path.relpath(patch.file, start=self.directory)],
                     stderr=stderr, cwd=self.directory)
        for file_name, (old_status, new_status) in self.status().items():
            if new_status == FileStatus.UNTRACKED and old_status == FileStatus.UNTRACKED \
                    and file_name.endswith(".porig"):
                # Remove wiggle's automatically created backup files
                # They're completely unessicary since the entire repo is version-controlled
                os.remove(path.join(self.directory, file_name))
        if result.returncode == 1:
            return False  # There were unresolved conflicts
        else:
            # Check for an unexpected error
            # Since conflicts were already checked for, this will only raise for unexpected errors
            result.check_returncode()
            return True  # Successfully wiggled

    def __str__(self):
        return path.basename(self.directory)

class PatchFile:
    def __init__(self, file):
        if not path.isfile(file):
            if not path.exists(file):
                raise ValueError("Patch file doesn't exist:", file)
            else:
                raise ValueError("Patch isn't a file:", file)
        self.file = file
        try:
            summary = run(["git", "apply", "--summary", file],
                          check=True, stdout=PIPE, universal_newlines=True).stdout
        except CalledProcessError:
            raise ValueError("Invalid patch file:", file)
        summary_pattern = re.compile(r"\s*(create) mode \d+ (\S+)")
        created_files = list()
        for line in summary.splitlines():
            match = summary_pattern.match(line)
            if not match:
                raise NotImplementedError("Don't know how to parse summary line: {}".format(line))
            (action, target_file) = match.groups()
            if action == "create":
                created_files.append(target_file)
        self.created_files = tuple(created_files)  # Immutable copy

    def __str__(self):
        return path.basename(self.file)

parser = ArgumentParser(description="Wiggle the patch into the specified git repository")
parser.add_argument("repo", help="The git repository to apply the patch to", type=GitRepository)
parser.add_argument("patch", help="The patch to apply to the repository", type=PatchFile)
parser.add_argument("--git-am", "--am", "-a", action="store_true",
                    help="If an automatic merge is in progress, continue it after wiggling")

args = parser.parse_args()

repository, patch = args.repo, args.patch

if not repository.is_clean():
    print(repository, "isn't a clean repo!")
    exit(1)


was_automatically_merging = False
if args.git_am and repository.is_automatically_merging():
    print("Automatic merge in progress, will continue applying if successful")
    was_automatically_merging = True

if not repository.wiggle_patch(patch):
    print("Unresolved conflicts found while wiggling!", file=stderr)
    print("Manual intervention is required to fix the conflicts!", file=stderr)
    exit(2)

if args.git_am and was_automatically_merging:
    assert repository.is_automatically_merging()
    try:
        print("Adding changed files to index")
        run(["git", "add", "."], stdout=stdout, stderr=stderr, check=True,
            cwd=repository.directory)
        print("Continuing automatic merge after successful wiggle")
        run(["git", "am", "--continue"], stdout=stdout, stderr=stderr, check=True,
            cwd=repository.directory)
    except CalledProcessError as e:
        print("Failed to continue automatic merge!", file=stderr)
        exit(3)
else:
    print("Successfully Wiggled", patch, "into", repository)
