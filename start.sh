#!/usr/bin/env bash
# exit on error
set -o errexit

# Run migrations (creates database tables)
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --no-input

# Start gunicorn
exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}
