FROM eclipse-temurin:11-jre-jammy

ARG SPARK_VERSION="spark-3.5.5"
ARG SPARK_FOLDER_NAME="${SPARK_VERSION}-bin-hadoop3.tgz"
ARG LINK_DOWNLOAD_SPARK="https://dlcdn.apache.org/spark/${SPARK_VERSION}/${SPARK_FOLDER_NAME}"

ENV SPARK_HOME="/opt/spark"
ENV SPARK_CONF_DIR="${SPARK_HOME}/conf/"
ENV SPARK_SBIN_DIR="${SPARK_HOME}/sbin/"
ENV SPARK_BIN_DIR="${SPARK_HOME}/bin/"
ENV SPARK_PYTHON_EXAMPLES="${SPARK_HOME}/examples/src/main/python/"
ENV SPARK_EVENTS_DIR="${SPARK_HOME}/spark-events/"
ENV PATH="${SPARK_HOME}:${SPARK_SBIN_DIR}:${SPARK_BIN_DIR}:${SPARK_EVENTS_DIR}:${PATH}"

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
    mkdir -p ${SPARK_EVENTS_DIR} && \
    wget -q ${LINK_DOWNLOAD_SPARK} -O ${SPARK_HOME}/${SPARK_FOLDER_NAME} && \
    tar xzf ${SPARK_HOME}/${SPARK_FOLDER_NAME} -C ${SPARK_HOME} --strip-components=1 && \
    rm -f ${SPARK_HOME}/${SPARK_FOLDER_NAME}
    
COPY entrypoint.sh ${SPARK_CONF_DIR}/entrypoint.sh
COPY spark-env.sh ${SPARK_CONF_DIR}/spark-env.sh
COPY spark-defaults.conf ${SPARK_CONF_DIR}/spark-defaults.conf

RUN chmod +x ${SPARK_CONF_DIR}/entrypoint.sh

ENTRYPOINT [ "bash", "-c", "$SPARK_HOME/bin/spark-submit --master spark://spark-master:7077 --deploy-mode client $SPARK_PYTHON_EXAMPLES/python/pi.py" ]