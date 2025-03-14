FROM ubuntu:22.04

RUN apt-get update -y && apt-get upgrade && apt-get install curl
RUN adduser --disable-password ubuntu && usermod -aG sudo ubuntu

RUN curl -fsSL https://code-server.dev/install.sh | sh

USER ubuntu
WORKDIR /home/ubuntu/projeto

EXPOSE 4277

CMD ["/usr/bin/code-server", "--bind-addr", "0.0.0.0:4277", "--auth", "none"]
