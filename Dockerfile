
FROM python:3.11-slim

# Upgrade pip and install runtime dependencies
RUN apt-get update && apt-get install -y gcc \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir gunicorn flask web3 openai requests \
    && apt-get remove -y gcc && apt-get autoremove -y && apt-get clean

WORKDIR /app
COPY . /app

EXPOSE 8501

CMD ["gunicorn", "--bind", "0.0.0.0:8501", "main:app"]
