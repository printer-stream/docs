# Build this image on top of the pre-built dependencies layer (Python packages +
# cached embedding model). Pass DEPS_IMAGE and DEPS_VERSION at build time to
# pin a specific release; the defaults here are fallbacks for local builds only.
ARG DEPS_IMAGE=ghcr.io/printer-stream/docs/mcp-dependencies-image
ARG DEPS_VERSION=1.1.0
FROM ${DEPS_IMAGE}:${DEPS_VERSION}

ARG APP_VERSION=dev
ARG VCS_REF=unknown
ARG BUILD_DATE=unknown

LABEL org.opencontainers.image.title="MCP Server" \
      org.opencontainers.image.description="Streamable-HTTP MCP server exposing hybrid FTS5 + vector search over printer specification documents" \
      org.opencontainers.image.authors="printer-stream" \
      org.opencontainers.image.source="https://github.com/printer-stream/docs" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /data

COPY ./index .
COPY ./md .
COPY ./md-bulk .
COPY ./jpeg .

WORKDIR /app

COPY ./mcp-server/* .

CMD ["python", "server.py"]
