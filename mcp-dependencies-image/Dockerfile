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
 && rm -rf /var/lib/apt/lists/*

# Build context is the repo root; requirements.txt lives in mcp-server/.
COPY mcp-server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the embedding model so the first server/indexer start is instant.
# The model is cached in HF_HOME and inherited by every image built FROM this one.
# (Local summarisation is opt-in — its model is fetched on demand at index time,
# not baked in here, to keep this shared layer slim.)
ARG DOCS_EMBED_MODEL=BAAI/bge-small-en-v1.5
ENV DOCS_EMBED_MODEL=${DOCS_EMBED_MODEL}
RUN python -c "import os; from sentence_transformers import SentenceTransformer; SentenceTransformer(os.environ['DOCS_EMBED_MODEL'])"
