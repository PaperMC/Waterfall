import io.papermc.fill.model.BuildChannel

// Waterfall is not a gradle project, we just use gradle to run the fill plugin for uploading artifacts
plugins {
    id("io.papermc.fill.gradle") version "1.0.3"
}

fill {
    project("waterfall")
    versionFamily("1.21")
    version("1.21")

    build {
        channel = BuildChannel.STABLE

        downloads {
            register("server:default") {
                file = file("Waterfall-Proxy/bootstrap/target/Waterfall.jar")
                nameResolver.set { project, _, version, build -> "$project-$version-$build.jar" }
            }
            for (module in listOf("cmd_alert", "cmd_find", "cmd_kick", "cmd_list", "cmd_send", "cmd_server", "reconnect_yaml")) {
                register("module:$module") {
                    file = file("Waterfall-Proxy/module/${module.replace("_", "-")}/target/$module.jar")
                    nameResolver.set { _, _, version, build -> "$module-$version-$build.jar" }
                }
            }
        }
    }
}
