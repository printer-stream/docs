# Extraction image: PDF -> jpeg + markdown + pagemap + quality.
# Runs locally or in CI; mount the repo at /work and pass --root /work.
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # Docling/HF model cache; mount a volume here in CI to avoid re-downloading.
    HF_HOME=/models

# tesseract is the OCR backend selected in convert.py (lighter than EasyOCR/torch
# defaults). libgl/libglib are needed by some imaging deps.
RUN apt-get update && apt-get install -y --no-install-recommends \
        tesseract-ocr \
        libtesseract-dev \
        libgl1 \
        libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default: run all phases over the whole corpus. Override args to run a single
# phase and/or a shard, e.g.:
#   docker run --rm -v "$PWD":/work img markdown --shard-index 0 --shard-count 4
ENTRYPOINT ["python", "-m", "extractor.cli", "--root", "/work"]
CMD ["run", "--all"]
