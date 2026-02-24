FROM jenkins/jenkins:lts

USER root
RUN apt-get update && \
    apt-get install -y docker.io docker-cli && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -for docker && \
    usermod -aG docker jenkins

USER jenkins
