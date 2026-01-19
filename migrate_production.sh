#!/bin/bash
# migrate_production.sh - Run migrations on production database

echo "🗄️  Running migrations on Neon Production Database..."
echo ""

# Set your Neon database URL
export DATABASE_URL="postgresql://neondb_owner:npg_NIuC8Sbt5aAD@ep-holy-cherry-a8c75a74-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

# Install dependencies if needed
echo "📦 Ensuring dependencies are installed..."
pip3 install -q psycopg2-binary dj-database-url

# Run migrations
echo ""
echo "🔄 Running database migrations..."
python3 manage.py migrate --noinput

echo ""
echo "✅ Migrations complete!"
echo ""
echo "👤 Now create your admin user:"
echo "   python3 manage.py createsuperuser"
echo ""
