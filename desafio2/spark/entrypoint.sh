#!/bin/bash
set -e

if [ -z "$SPARK_MODE" ]; then
    echo "A variável de ambiente SPARK_MODE não está definida. Defina SPARK_MODE como 'master', 'worker' ou 'history'."
    exit 1
fi
if [ "$SPARK_MODE" == "master" ]; then
    echo "Iniciando o Spark Master..."
    bash $SPARK_SBIN_DIR/start-master.sh -p 7077

elif [ "$SPARK_MODE" == "worker" ]; then
    echo "Iniciando o Spark Worker..."
    bash $SPARK_SBIN_DIR/start-worker.sh spark://spark-master:7077

elif [ "$SPARK_MODE" == "history" ]
then
    echo "Iniciando o Spark History..."
    bash $SPARK_BIN_DIR/spark-submit --master spark://spark-master:7077 --deploy-mode client $SPARK_PYTHON_EXAMPLES/pi.py && $SPARK_SBIN_DIR/start-history-server.sh
else
    echo "Valor inválido para SPARK_MODE. Use 'master', 'worker', 'history' ou 'spark-shell'."
    exit 1
fi
