FROM python:3.11-slim
RUN apt-get update && apt-get install -y gcc \
 && pip install --upgrade pip \
 && pip install --no-cache-dir flask gunicorn requests web3 openai \
 && apt-get remove -y gcc && apt-get autoremove -y && apt-get clean
WORKDIR /app
COPY . /app
EXPOSE 8501
CMD ["gunicorn", "--bind", "0.0.0.0:8501", "main:app"]
