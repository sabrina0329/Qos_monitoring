# ------------------------------------------------------------
# Dockerfile for Apache NiFi 2.3.0
# Includes setup for volumes used in docker-compose
# ------------------------------------------------------------

# 1. Base image
ARG NIFI_VERSION=2.3.0
FROM apache/nifi:${NIFI_VERSION}

# 2. Switch to root to make config changes
USER root

# 3. Copy initial flow if needed (optional)
COPY flow.json.gz /opt/nifi/nifi-current/conf/flow.json.gz

# 4. Set permissions for NiFi to access the flow file
RUN chown nifi:nifi /opt/nifi/nifi-current/conf/flow.json.gz && \
    chmod 644 /opt/nifi/nifi-current/conf/flow.json.gz

# 5. Create required folders for NiFi repositories and data paths (if they don’t exist via volume)
# Note: These will be overridden if volumes are mounted at runtime
RUN mkdir -p \
    /data/landing \
    /data/success \
    /data/failure \
    /data/joblogs && \
    chown -R nifi:nifi \
      /opt/nifi/nifi-current/database_repository \
      /opt/nifi/nifi-current/flowfile_repository \
      /opt/nifi/nifi-current/content_repository \
      /opt/nifi/nifi-current/provenance_repository \
      /opt/nifi/nifi-current/state \
      /data && \
    chmod -R 777 /data

# 6. Revert to nifi user
USER nifi

# 7. Default command (can be overridden by compose)
CMD ["bin/nifi.sh", "run"]
