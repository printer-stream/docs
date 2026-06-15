FROM python:3.13-slim

ARG APP_VERSION=dev
ARG VCS_REF=unknown
ARG BUILD_DATE=unknown

LABEL org.opencontainers.image.title="MCP Dependencies" \
      org.opencontainers.image.description="Python runtime and packages for the printer-stream FTS5 MCP server" \
      org.opencontainers.image.authors="printer-stream" \
      org.opencontainers.image.source="https://github.com/printer-stream/docs" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /app

# Search is pure FTS5 (Python's bundled SQLite has FTS5 enabled), and the slim
# requirements install from wheels, so no compiler toolchain is needed. The
# sqlite3 CLI is kept only for inspecting the committed index during ops.
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
 && rm -rf /var/lib/apt/lists/*

# Build context is the repo root; requirements.txt lives in mcp-server/.
COPY mcp-server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
