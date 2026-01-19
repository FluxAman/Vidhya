#!/bin/bash
# Quick Setup Script for Vercel Deployment
# This script helps you prepare your local environment

echo "🚀 Vidya Bharti - Vercel Deployment Setup"
echo "=========================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found: $PYTHON_VERSION"
else
    echo "❌ Python 3 not found. Please install Python 3.11+"
    exit 1
fi

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Check if .env exists
echo ""
if [ -f ".env" ]; then
    echo "✅ .env file exists"
else
    echo "⚠️  .env file not found. Creating from .env.example..."
    cp .env.example .env
    echo "📝 Please edit .env with your configuration"
fi

# Generate secret key if needed
echo ""
echo "🔑 Generate a new SECRET_KEY for production:"
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

echo ""
echo "✅ Setup complete!"
echo ""
echo "📚 Next Steps:"
echo "1. Edit .env with your settings (use SECRET_KEY above)"
echo "2. Run: python3 manage.py migrate"
echo "3. Run: python3 manage.py createsuperuser"
echo "4. Run: python3 manage.py collectstatic --noinput"
echo "5. Test: python3 manage.py runserver"
echo ""
echo "🌐 For Vercel deployment, see DEPLOYMENT.md"
echo ""
