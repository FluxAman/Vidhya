#!/bin/bash
# Build script for Vercel deployment
# This runs in Vercel's own Python environment — no pip install needed

set -e

echo "=== Collecting static files ==="
python3 manage.py collectstatic --noinput

echo "=== Running database migrations ==="
python3 manage.py migrate --noinput

echo "=== Build complete ==="
