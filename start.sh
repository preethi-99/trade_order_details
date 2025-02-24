#!/bin/sh

# Wait for PostgreSQL to become available
echo "Waiting for PostgreSQL..."

while ! nc -z db 5432; do
  sleep 0.5
done

echo "PostgreSQL started"

# Run migrations if you have any setup scripts
python setup.py

# Start Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
