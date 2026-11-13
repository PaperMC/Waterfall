import io.papermc.fill.model.BuildChannel

// Waterfall is not a gradle project, we just use gradle to run the fill plugin for uploading artifacts
plugins {
    id("io.papermc.fill.gradle") version "1.0.6"
}

fill {
    project("waterfall")
    versionFamily("26")
    version("26.1")

    build {
        channel = BuildChannel.STABLE

        downloads {
            register("server:default") {
                file = file("Waterfall-Proxy/bootstrap/target/Waterfall.jar")
                nameResolver.set { project, _, version, build -> "$project-$version-$build.jar" }
            }
            // Modules are bundled inside the server jar and extracted at startup, so they are no longer published separately
        }
    }
}
