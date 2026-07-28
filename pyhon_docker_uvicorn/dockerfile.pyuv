# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Flask port
EXPOSE 8000

# Start the application with Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
# CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "app:app"]

CMD ["gunicorn", "--workers", "4","--threads", "2", "--bind", "0.0.0.0:8000", "app:app" ]