ARG DEPS_IMAGE=ghcr.io/printer-stream/docs/mcp-dependencies-image
ARG DEPS_VERSION=1.2.0
FROM ${DEPS_IMAGE}:${DEPS_VERSION}

ARG APP_VERSION=dev
ARG VCS_REF=unknown
ARG BUILD_DATE=unknown

LABEL org.opencontainers.image.title="MCP Index" \
      org.opencontainers.image.description="Python runtime, packages, and pre-cached embedding model for the printer-stream MCP indexer" \
      org.opencontainers.image.authors="printer-stream" \
      org.opencontainers.image.source="https://github.com/printer-stream/docs" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /app

# Pre-download the embedding model so the first server/indexer start is instant.
# The model is cached in HF_HOME and inherited by every image built FROM this one.
# (Local summarisation is opt-in — its model is fetched on demand at index time,
# not baked in here, to keep this shared layer slim.)
ARG DOCS_EMBED_MODEL=BAAI/bge-small-en-v1.5
ENV DOCS_EMBED_MODEL=${DOCS_EMBED_MODEL}
RUN python -c "import os; from sentence_transformers import SentenceTransformer; SentenceTransformer(os.environ['DOCS_EMBED_MODEL'])"
