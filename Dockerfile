# Railpack/mise has no precompiled binary for the pinned legacy Python, so the
# image build exits before pip runs. This image keeps Django 2.2 on Python 3.9.
FROM python:3.9.25-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x start.sh

CMD ["./start.sh"]
