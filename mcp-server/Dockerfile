# Built on top of the pre-built dependencies layer (Python packages + cached
# embedding model). Build context is the REPO ROOT (see build-mcp-server.yml),
# so the committed data tree can be baked in alongside the app code.
# Pass DEPS_IMAGE / DEPS_VERSION at build time to pin a release; the defaults
# here are fallbacks for local builds only.
ARG DEPS_IMAGE=ghcr.io/printer-stream/docs/mcp-dependencies-image
ARG DEPS_VERSION=1.2.0
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

# Self-contained data tree at /data (matches DOCS_REPO_ROOT). Baked in so the
# server needs no external volume on render.com. Each COPY keeps its directory
# name so the repo-relative image paths stored in the index still resolve
# (index/specs.db, md/<vendor>/..., jpeg/<vendor>/...).
WORKDIR /data
COPY ./index ./index
COPY ./md ./md
COPY ./md-bulk ./md-bulk
COPY ./jpeg ./jpeg

# Application code (the mcp-server package lands directly in /app).
WORKDIR /app
COPY ./mcp-server/ ./

# FastMCP binds to PORT (render injects it); 8000 is the local default.
EXPOSE 8000

CMD ["python", "server.py"]
