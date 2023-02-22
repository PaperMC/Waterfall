Waterfall
=========

Waterfall is a fork of the well-known [BungeeCord](https://github.com/SpigotMC/BungeeCord) server teleportation suite.

Waterfall focuses on three main areas:

- **Stability**: Waterfall aims to be stable. We will achieve this through making the code base testable and discouraging practices that lead to proxy lag.
- **Features**: Waterfall aims to include more features than canonical BungeeCord.
- **Scalability**: Waterfall should be able to handle a large number of concurrent players, given a reasonably modern CPU, memory, and good network connection.

## Why fork BungeeCord?

Think of Waterfall as a principles fork.

Waterfall was forked because of the fact that upstream does not accept many contributions that are intended to better the ecosystem. Simply put, Waterfall aims to better
the ecosystem by allowing changes to be exposed to a wider audience more quickly.

Waterfall will still track upstream BungeeCord and merge changes as needed.

## How To (Server Admins)

Download a copy of Waterfall.jar from our homepage here: [Waterfall](https://papermc.io/downloads#Waterfall)

Waterfall requires **Java 8** or above.

## How To (Plugin Developers)
------
 * See our API patches [here](BungeeCord-Patches)
 * Waterfall API JavaDocs here: [papermc.io/javadocs](https://papermc.io/javadocs)
 * Maven repository (for `waterfall-api`):
```xml
<repository>
    <id>papermc</id>
    <url>https://repo.papermc.io/repository/maven-public/</url>
</repository>
```
 * Artifact information:
```xml
<dependency>
    <groupId>io.github.waterfallmc</groupId>
    <artifactId>waterfall-api</artifactId>
    <version>1.19-R0.1-SNAPSHOT</version>
    <scope>provided</scope>
</dependency>
 ```

**Or alternatively, with Gradle:**

 * Repository:
```groovy
repositories {
    maven {
        url 'https://repo.papermc.io/repository/maven-public/'
    }
}
```
 * Artifact:
```groovy
dependencies {
    compileOnly 'io.github.waterfallmc:waterfall-api:1.19-R0.1-SNAPSHOT'
}
```

## How To (Compiling From Source)

To compile Waterfall, you need JDK8, git, bash, maven, and an internet connection.

Clone this repo, run `./waterfall b` from *bash*, get jar from Waterfall-Proxy/bootstrap/target/

## Join us

* Feel free to open a PR! We accept contributions.
* Join us on IRC (irc.esper.net #waterfall, [webchat](https://webchat.esper.net/?channels=waterfall)) or [Discord](https://discord.gg/papermc).
* Visit our forums (https://papermc.io/forums).

## Special Thanks To

![YourKit-Logo](https://yourkit.com/images/yklogo.png)

[YourKit](https://yourkit.com/), makers of the outstanding Java profiler, supports open source projects of all kinds with their full-featured [Java](https://yourkit.com/features/) and [.NET](https://yourkit.com/dotnet/features/) application profilers. We thank them for granting Waterfall an OSS license so that we can make our software the best it can be.
