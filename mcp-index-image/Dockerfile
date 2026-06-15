ARG DEPS_IMAGE=ghcr.io/printer-stream/docs/mcp-dependencies-image
ARG DEPS_VERSION=1.2.0
FROM ${DEPS_IMAGE}:${DEPS_VERSION}

ARG APP_VERSION=dev
ARG VCS_REF=unknown
ARG BUILD_DATE=unknown

LABEL org.opencontainers.image.title="MCP Index" \
      org.opencontainers.image.description="Python runtime and packages for the printer-stream FTS5 MCP indexer" \
      org.opencontainers.image.authors="printer-stream" \
      org.opencontainers.image.source="https://github.com/printer-stream/docs" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /app

# Indexing is pure FTS5 — no embedding model to pre-cache. This image is now a
# thin pin over the dependencies layer so the search-index workflow keeps a
# stable, versioned runtime for `python mcp-server/indexer.py`.
