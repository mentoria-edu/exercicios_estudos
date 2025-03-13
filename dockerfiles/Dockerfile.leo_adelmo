FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y && apt-get install curl -y
RUN adduser --disabled-password admin && usermod -aG sudo admin
RUN curl -fsSL https://code-server.dev/install.sh | sh

USER admin
WORKDIR /home/admin

VOLUME /home/admin/projetos_mentoria

EXPOSE 4277

CMD ["/usr/bin/code-server", "--bind-addr", "0.0.0.0:4277", "--auth", "none"]
