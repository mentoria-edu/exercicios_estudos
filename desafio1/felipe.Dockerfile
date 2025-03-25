FROM    ubuntu:22.04


RUN     apt-get update && \
        apt-get upgrade -y &&\
        apt-get install -y curl &&\
        apt-get install -y sudo

RUN     adduser kakuna &&\
        usermod -aG sudo kakuna

RUN     curl -fsSL https://code-server.dev/install.sh | sh

RUN     mkdir -p /home/kakuna/.config/code-server
RUN     echo "bind-addr: 0.0.0.0:4277\nauth: none\ncert: false" > /home/kakuna/.config/code-server/config.yaml

EXPOSE  4277

USER    kakuna

CMD     ["code-server"]
