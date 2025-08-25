# Base image
FROM python:3.11-slim

# Prevents Python from writing pyc files and enables unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy dependency file first for better caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Expose port (matches Config.PORT)
EXPOSE 8080

# Healthcheck (basic TCP check)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import socket,sys;s=socket.socket();s.settimeout(3);s.connect(('127.0.0.1',8080));s.close()" || exit 1

# Default command
CMD ["python", "app.py"]


