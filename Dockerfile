# Use a slim and secure base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the correct port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "Secure_Live_ROI_Dashboard_Encrypted.py", "--server.port=8501", "--server.enableCORS=false"]
