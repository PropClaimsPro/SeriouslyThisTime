# Use a slim and secure base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install all dependencies including Qiskit and FastAPI
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose the port
EXPOSE 8000

# Run the FastAPI app using Gunicorn with Uvicorn worker
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "api.main:app", "-k", "uvicorn.workers.UvicornWorker"]
