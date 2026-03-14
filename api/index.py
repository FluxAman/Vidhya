"""
Vercel serverless entrypoint for Django.

This file:
1. Runs database migrations automatically on the first cold-start
2. Ensures admin superuser always has the correct password
3. Exposes the Django WSGI application as the Vercel handler
"""

import os
import sys

# Ensure the project root is in the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Run migrations automatically so that the database is always up-to-date
# on Vercel cold-starts.  This is safe because migrate is idempotent.
_migrations_run = False


def run_migrations():
    global _migrations_run
    if not _migrations_run:
        import django
        django.setup()
        from django.core.management import call_command
        try:
            call_command('migrate', '--noinput', verbosity=0)
        except Exception as exc:
            print(f"[Vercel] Migration warning: {exc}", file=sys.stderr)

        # Always ensure admin superuser exists with the correct password.
        # Uses get_or_create + set_password so that even if a broken user
        # was created by a previous failed deployment, it gets fixed.
        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@vidhya.in',
                    'is_staff': True,
                    'is_superuser': True,
                }
            )
            # Always reset the password to guarantee login works
            user.set_password('Admin@123')
            user.is_staff = True
            user.is_superuser = True
            user.save()
            action = 'created' if created else 'password-reset'
            print(f"[Vercel] Admin superuser {action}: admin / Admin@123", file=sys.stderr)
        except Exception as exc:
            print(f"[Vercel] Superuser warning: {exc}", file=sys.stderr)

        _migrations_run = True


# Run migrations before the first request is handled
run_migrations()

# Import the WSGI application
from config.wsgi import application  # noqa: E402
