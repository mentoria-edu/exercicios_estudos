FROM ubuntu:22.04

RUN apt update -y && apt upgrade -y && \
    apt install -y curl sudo

RUN useradd -m -s /bin/bash ubuntu && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER ubuntu

WORKDIR /home/ubuntu/projects

RUN curl -fsSL https://code-server.dev/install.sh | sh

EXPOSE 4277

CMD ["code-server", "--bind-addr", "0.0.0.0:4277", "--auth", "none"]