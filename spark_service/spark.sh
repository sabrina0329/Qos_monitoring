#!/bin/bash

# Configuration
SPARK_HOME="/opt/bitnami/spark"
JAR_PATH="/data/shared/Parse3GPPXML-assembly-1.0.jar"
INPUT_PATH="/data/shared/xml_input"
OUTPUT_PATH="/data/shared/json_output"
CLASS_NAME="Parse3GPPXML"

# Créer le dossier de sortie si besoin
mkdir -p "$OUTPUT_PATH"

# Vérifier si le Spark Master est accessible
timeout 5 bash -c "</dev/tcp/spark-master/7077" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "==> Spark Master détecté, exécution en mode cluster..."
    "$SPARK_HOME/bin/spark-submit" \
        --class "$CLASS_NAME" \
        --master spark://spark-master:7077 \
        --deploy-mode client \
        "$JAR_PATH" \
        "$INPUT_PATH" \
        "$OUTPUT_PATH"
else
    echo "==> Spark Master non détecté, exécution en mode local..."
    "$SPARK_HOME/bin/spark-submit" \
        --class "$CLASS_NAME" \
        --master local[2] \
        "$JAR_PATH" \
        "$INPUT_PATH" \
        "$OUTPUT_PATH"
fi
