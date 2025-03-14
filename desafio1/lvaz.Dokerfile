FROM ubuntu:22.04

RUN adduser --gecos "" --disabled-password ubuntu && usermod -aG sudo ubuntu

RUN apt-get update 

RUN apt install -y curl 

RUN curl -fsSL https://code-server.dev/install.sh | sh 

EXPOSE 4277

USER ubuntu

CMD ["code-server", "--bind-addr", "0.0.0.0:4277", "--auth", "none", "--cert", "false"]
