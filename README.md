FlameCord
=======

FlameCord is a patch for FlameCord to fix possible exploits and add useful functionalities.

FlameCord is compiled like FlameCord does; Please follow the CONTRIBUTING.md file. If you need help you can always contact us on Discord.

To compile FlameCord you need the same requirements as FlameCord, and run the command `./flamecord b` to get the corresponding jar.

<a href="https://discord.gg/gF36AT3"><img src="https://discord.com/assets/4ff060e44afc171e9622fbe589c2c09e.png" width=10% height=10%><img/><a/> <a href="https://www.mc-market.org/resources/13492/"><img src="https://www.mc-market.org/styles/mcmarketv2/xenforo/logo.png" width=10% height=10%><img/><a/>

FlameCord [![Build Status](https://papermc.io/ci/job/FlameCord/badge/icon)](https://papermc.io/ci/job/FlameCord/)
=======

FlameCord is Waterfall with additional protocols. Waterfall is a fork of the well-known [BungeeCord](https://github.com/SpigotMC/BungeeCord) server teleportation suite.

Waterfall focuses on three main areas:

* **Stability**: Waterfall aims to be stable. We will achieve this through making the code base testable and discouraging practices that lead to proxy lag.
* **Features**: Waterfall aims to include more features than canonical BungeeCord.
* **Scalability**: Waterfall should be able to handle a large number of concurrent players, given a reasonably modern CPU, memory, and good network connection.

FlameCord focuses on one main area:

* **Additional Client Version Support**: FlameCord aims to support client versions older then what is supported in upstream. This includes 1.7 support. Additionally FlameCord may release Snapshot and PRE Client support patches as time permits.

## Why fork Waterfall?

FlameCord has a goal of adding additional protocol versions.

FlameCord was forked because of the fact that Waterfall intends to only support protocol versions supported by upstream BungeeCord. 

FlameCord will track upstream Waterfall and merge changes as needed.

## How to (Server Admins)

Download a copy of FlameCord.jar from our homepage here: [FlameCord](https://papermc.io/downloads#FlameCord)

FlameCord requires **Java 8** or above.

## How To (Compiling from source)

To compile FlameCord, you need JDK8, git, bash, maven, and an internet connection.

Clone this repo, run `./flamecord b` from *bash*, get jar from `FlameCord-Proxy/bootstrap/target`

## Join us

* Feel free to open a PR! We accept contributions.
* Join us on IRC (irc.spi.gt #paper, [webchat](http://irc.spi.gt/iris/?nick=&channels=paper)).
* Visit our forums (https://papermc.io/forums).

Special Thanks To
-----------------
![YourKit-Logo](https://yourkit.com/images/yklogo.png)

[YourKit](https://yourkit.com/), makers of the outstanding Java profiler, supports open source projects of all kinds with their full-featured [Java](https://yourkit.com/features/) and [.NET](https://yourkit.com/dotnet/features/) application profilers. We thank them for granting FlameCord an OSS license so that we can make our software the best it can be.
