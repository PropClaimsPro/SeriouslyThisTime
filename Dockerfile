# Use a slim Python image
FROM python:3.11-slim

# Install system dependencies and upgrade pip
RUN apt-get update && apt-get install -y gcc \
  && pip install --upgrade pip \
  && pip install --no-cache-dir gunicorn flask web3 openai requests \
  && apt-get remove -y gcc && apt-get autoremove -y && apt-get clean

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Expose port 8501 for health checks and traffic
EXPOSE 8501

# Run app with Gunicorn and Flask on port 8501
CMD ["gunicorn", "--bind", "0.0.0.0:8501", "main:app"]
