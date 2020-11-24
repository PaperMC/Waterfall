FROM openjdk:11

# Define the environment variables
ENV USER=container
ENV SERVER_DIRECTORY="/home/container"

ENV JAVA_HEAP_SIZE="4G"
ENV JAVA_ARGUMENTS="-Xmx${JAVA_HEAP_SIZE} -Xms${JAVA_HEAP_SIZE}"

# Create a user so we don't run as root
RUN addgroup ${USER} && \
    useradd -ms /bin/bash ${USER} -g ${USER} -d ${SERVER_DIRECTORY} && \
    chown -R ${USER}:${USER} ${SERVER_DIRECTORY}
USER ${USER}

WORKDIR $SERVER_DIRECTORY

COPY Waterfall-Proxy/bootstrap/target/Waterfall.jar server.jar

ENTRYPOINT [ "java", "-jar", "server.jar" ]
