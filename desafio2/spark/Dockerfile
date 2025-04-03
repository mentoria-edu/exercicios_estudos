FROM eclipse-temurin:11-jre-jammy

ARG LINK_DOWNLOAD_SPARK='https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz'
ARG SPARK_FOLDER_NAME='spark-3.5.5-bin-hadoop3.tgz'

ENV SPARK_HOME="/opt/spark"
ENV SPARK_CONF_DIR="${SPARK_HOME}/conf"
ENV PATH="${SPARK_HOME}/sbin:${SPARK_HOME}/bin:${PATH}"

RUN apt update -y && \
    apt install -y --no-install-recommends \
    python3 \
    rsync \
    wget \
    ssh \
    tini \
    krb5-user \
    libnss3  \
    net-tools && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${SPARK_HOME} && \
    mkdir -p ${SPARK_HOME}/spark-events && \
    wget -q ${LINK_DOWNLOAD_SPARK} -O ${SPARK_HOME}/${SPARK_FOLDER_NAME} && \
    tar xzf ${SPARK_HOME}/${SPARK_FOLDER_NAME} -C ${SPARK_HOME} --strip-components=1 && \
    rm -f ${SPARK_HOME}/${SPARK_FOLDER_NAME}
    
COPY entrypoint.sh ${SPARK_CONF_DIR}/entrypoint.sh
COPY spark-env.sh ${SPARK_CONF_DIR}/spark-env.sh
COPY spark-defaults.conf ${SPARK_CONF_DIR}/spark-defaults.conf

ENTRYPOINT [ "bash", "${SPARK_CONF_DIR}/entrypoint.sh" ]