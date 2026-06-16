# Indexing image: markdown + pagemap -> SQLite FTS5 search index.
# Pure standard library; the base image's bundled SQLite provides FTS5 + trigram.
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY . .

# Fail fast at build time if the bundled SQLite lacks FTS5 or the trigram tokenizer.
RUN python -c "import sqlite3; c=sqlite3.connect(':memory:'); \
c.execute('CREATE VIRTUAL TABLE a USING fts5(x)'); \
c.execute('CREATE VIRTUAL TABLE b USING fts5(x, tokenize=\"trigram\")'); \
print('sqlite', sqlite3.sqlite_version, 'fts5+trigram OK')"

# Mount the repo at /work; build reads data-extraction/ and writes the index there.
ENTRYPOINT ["python", "-m", "indexer.cli", "--root", "/work"]
CMD ["build"]
