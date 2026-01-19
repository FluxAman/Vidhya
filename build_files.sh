#!/usr/bin/env bash
# Build script for Vercel deployment
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

echo "Build complete!"
