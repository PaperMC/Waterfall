#!/usr/bin/env bash
(
set -e
PS1="$"

function changelog() {
    base=$(git ls-tree HEAD $1  | cut -d' ' -f3 | cut -f1)
    cd $1 && git log --oneline ${base}...HEAD
}
bungee=$(changelog BungeeCord)

updated=""
logsuffix=""
if [ ! -z "$bungee" ]; then
    logsuffix="$logsuffix\n\nBungeeCord Changes:\n$bungee"
    if [ -z "$updated" ]; then updated="BungeeCord"; else updated="$updated/BungeeCord"; fi
fi
disclaimer="Upstream has released updates that appear to apply and compile correctly.\nThis update has not been tested by PaperMC and as with ANY update, please do your own testing"

if [ ! -z "$1" ]; then
    disclaimer="$@"
fi

log="${UP_LOG_PREFIX}Updated Upstream ($updated)\n\n${disclaimer}${logsuffix}"

echo -e "$log" | git commit -F -

) || exit 1
