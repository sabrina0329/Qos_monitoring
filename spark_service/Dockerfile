FROM bitnami/spark:3.5.0

# Install necessary packages including netcat for network testing
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    netcat-openbsd \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python dependencies first (for better caching)
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY spark.sh .
COPY spark_service.py .
COPY Parse3GPPXML-assembly-1.0.jar .

# Make spark.sh executable
RUN chmod +x spark.sh

# Create necessary directories and ensure proper permissions
RUN mkdir -p /data/shared && \
    mkdir -p /tmp && \
    chmod 777 /data/shared

EXPOSE 5000

# Copy JAR to shared directory and start the service
CMD ["bash", "-c", "cp /app/Parse3GPPXML-assembly-1.0.jar /data/shared/ && python3 spark_service.py"]