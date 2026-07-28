# -----------------------------
# Stage 1: Python + Gunicorn
# -----------------------------
FROM python:3.12-slim AS python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# -----------------------------
# Stage 2: Nginx
# -----------------------------
FROM nginx:latest

# Copy Python runtime
COPY --from=python /usr/local /usr/local

# Copy application
COPY --from=python /app /app

WORKDIR /app

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD sh -c "\
gunicorn \
    --workers 4 \
    --threads 2 \
    --bind 127.0.0.1:8000 \
    app:app \
& \
nginx -g 'daemon off;'"