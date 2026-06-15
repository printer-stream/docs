FROM python:3.13-slim

ARG APP_VERSION=dev
ARG VCS_REF=unknown
ARG BUILD_DATE=unknown

LABEL org.opencontainers.image.title="MCP Dependencies" \
      org.opencontainers.image.description="Python runtime, packages, and pre-cached embedding model for the printer-stream MCP server" \
      org.opencontainers.image.authors="printer-stream" \
      org.opencontainers.image.source="https://github.com/printer-stream/docs" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    sqlite3 \
    libsqlite3-dev \
    cmake \
 && rm -rf /var/lib/apt/lists/*

# Build context is the repo root; requirements.txt lives in mcp-server/.
COPY mcp-server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
