FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y curl sudo

RUN useradd -m -s /bin/bash devadmin && usermod -aG sudo devadmin

RUN curl -fsSL https://code-server.dev/install.sh | bash

USER devadmin
WORKDIR /home/devadmin

VOLUME /home/devadmin/workspace

EXPOSE 4277

CMD ["/usr/bin/code-server", "--bind-addr", "0.0.0.0:4277", "--auth", "none"]

