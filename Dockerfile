# ✅ Use slim Python base image
FROM python:3.11-slim

# ✅ Upgrade pip and install gunicorn + dependencies
RUN apt-get update && apt-get install -y gcc \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir flask gunicorn web3 openai requests \
    && apt-get remove -y gcc && apt-get autoremove -y && apt-get clean

# ✅ Set working directory
WORKDIR /app

# ✅ Copy app contents
COPY . /app

# ✅ Expose port used by Flask app (DigitalOcean default health check port)
EXPOSE 8501

# ✅ Run with Gunicorn for production Flask (better health check support)
CMD ["gunicorn", "--bind", "0.0.0.0:8501", "main:app"]
