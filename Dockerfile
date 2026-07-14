FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt requirements-dev.txt ./
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements-dev.txt

COPY data/ ./data/
COPY notebooks/ ./notebooks/
COPY tests/ ./tests/

CMD ["pytest", "-q"]

