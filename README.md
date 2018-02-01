# Travertine <a href="https://ci.destroystokyo.com/job/Travertine/"><img src="https://ci.destroystokyo.com/job/Paper/badge/icon"/></a>

Travertine is Waterfall with additional protocols. Waterfall is a fork of the well-known [BungeeCord](https://github.com/SpigotMC/BungeeCord) server teleportation suite.

Waterfall focuses on three main areas:

* **Stability**: Waterfall aims to be stable. We will achieve this through making the code base testable and discouraging practices that lead to proxy lag.
* **Features**: Waterfall aims to include more features than canonical BungeeCord.
* **Scalability**: Waterfall should be able to handle a large number of concurrent players, given a reasonably modern CPU, memory, and good network connection.

Travertine focuses on one main area:

* **Additional Client Version Support**: Travertine aims to support client versions older then what is supported in upstream. This includes 1.7 support. Additionally Travertine may release Snapshot and PRE Client support patches as time permits.

## Why fork Waterfall?

Travertine has a goal of adding additional protocol versions.

Travertine was forked because of the fact that Waterfall intends to only support protocol versions supported by upstream BungeeCord. 

Travertine will track upstream Waterfall and merge changes as needed.

## How to (Server Admins)

Download a copy of of Travertine.jar from our buildserver here: [Travertine](https://ci.destroystokyo.com/job/Travertine)

Travertine requires **java 8** or above.

## How To (Compiling from source)

To compile Travertine, you need JDK8, git, bash, maven, and an internet connection.

Clone this repo, run `./build.sh` from *bash*, get jar from `Travertine-Proxy/bootstrap/target`

## Join us

* Feel free to open a PR! We accept contributions.
* Join us on IRC (irc.esper.net #waterfall, [webchat](http://webchat.esper.net/?nick=&channels=waterfall)).
* Visit our forums on [Aquifer](https://aquifermc.org).

Special Thanks To
-----------------
![YourKit-Logo](https://yourkit.com/images/yklogo.png)

[YourKit](https://yourkit.com/), makers of the outstanding Java profiler, supports open source projects of all kinds with their full-featured [Java](https://yourkit.com/features/) and [.NET](https://yourkit.com/dotnet/features/) application profilers. We thank them for granting Waterfall an OSS license so that we can make our software the best it can be.
