FROM ubuntu:22.04

RUN apt update && apt install -y sudo curl

RUN adduser --disabled-password dev && usermod -aG sudo dev

RUN curl -fsSL https://code-server.dev/install.sh | sh

EXPOSE 4277

USER dev

WORKDIR /home/dev/workspace

CMD ["code-server", "--bind-addr", "0.0.0.0:4277", "--auth", "none"]

