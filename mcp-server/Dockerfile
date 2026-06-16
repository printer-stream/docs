# MCP server. Build context is the REPO ROOT (needs data-extraction/):
#   docker build -f mcp-server/Dockerfile --target lean    -t mcp-server:<ver> .
#   docker build -f mcp-server/Dockerfile --target stuffed -t mcp-server:<ver>-stuffed .
#
# Both variants bake the search index. The lean variant serves no static files
# (use DOCS_STATIC_BASE_URL for a CDN, or mount a volume at /app/static). The
# stuffed variant additionally bakes jpeg + markdown and serves them itself.

FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    DOCS_DB_PATH=/app/index/specs.db \
    DOCS_STATIC_DIR=/app/static \
    PORT=10000

WORKDIR /app

COPY mcp-server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp-server/ /app/
# Search index is baked into every variant.
COPY data-extraction/index/fulltext/specs.db /app/index/specs.db

EXPOSE 10000
CMD ["sh", "-c", "uvicorn app.server:app --host 0.0.0.0 --port ${PORT}"]


# Lean: index only, no static assets baked.
FROM base AS lean


# Stuffed: also bake jpeg + markdown so the image is fully self-contained.
FROM base AS stuffed
COPY data-extraction/jpeg /app/static/jpeg
COPY data-extraction/markdown /app/static/markdown
