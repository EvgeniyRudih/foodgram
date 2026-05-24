FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "\
  echo 'Waiting for database...' && \
  while ! python -c \"import os; import psycopg2; psycopg2.connect(host=os.environ['DB_HOST'], dbname=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'], port=os.environ.get('DB_PORT', 5432))\" 2>/dev/null; do \
    echo 'DB not ready, retrying in 2s...'; sleep 2; \
  done && \
  echo 'DB is ready!' && \
  python manage.py migrate --noinput && \
  python manage.py collectstatic --noinput && \
  gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000 \
"]