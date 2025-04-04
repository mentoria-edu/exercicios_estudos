FROM ubuntu:22.04

ARG V_HADOOP=3.4.1
ARG HADOOP_DIR=/opt/hadoop
ARG V_JAVA=8


ENV HADOOP_HOME=${HADOOP_DIR}
ENV USER_HDFS=hdfs
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV JAVA_VERSION=${V_JAVA}
ENV JAVA_HOME=/usr/lib/jvm/java-$JAVA_VERSION-openjdk-amd64
ENV USER_HOME=/home/$USER_HDFS
ENV HDFS_NAMENODE_USER=$USER_HDFS
ENV HDFS_DATANODE_USER=$USER_HDFS
ENV HDFS_SECONDARYNAMENODE_USER=$USER_HDFS

RUN apt update && apt install -y \
    openjdk-$JAVA_VERSION-jdk \
    wget \
    sudo \
    openssh-client \
    openssh-server

RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-${V_HADOOP}/hadoop-${V_HADOOP}.tar.gz && \
    tar -xvzf hadoop-${V_HADOOP}.tar.gz -C /opt && \
    mv /opt/hadoop-${V_HADOOP} $HADOOP_HOME

RUN echo "export JAVA_HOME=${JAVA_HOME}" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh

RUN adduser --gecos "" --disabled-password $USER_HDFS && \
    usermod -aG sudo $USER_HDFS && \
    chown -R $USER_HDFS:$USER_HDFS ${USER_HOME} && \
    adduser --gecos "" --disabled-password hive 

RUN chown -R $USER_HDFS:$USER_HDFS $HADOOP_HOME

RUN hdfs namenode -format

RUN mkdir -p $USER_HOME/.ssh && \
    ssh-keygen -t rsa -P '' -f $USER_HOME/.ssh/id_rsa && \
    cat $USER_HOME/.ssh/id_rsa.pub >> $USER_HOME/.ssh/authorized_keys && \
    chmod 700 $USER_HOME/.ssh && \
    chmod 600 $USER_HOME/.ssh/authorized_keys && \
    chown -R $USER_HDFS:$USER_HDFS $USER_HOME/.ssh

COPY core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml

RUN mkdir -p $HADOOP_HOME/logs && chown -R $USER_HDFS:$USER_HDFS $HADOOP_HOME/logs

EXPOSE 9870 9864

COPY entrypoint.sh /etc/entrypoint.sh

ENTRYPOINT ["sh", "/etc/entrypoint.sh"]
