# Vidya Bharti Awasiya Vidyalaya - School Management System

A comprehensive Django-based school management system for **Vidya Bharti Awasiya Vidyalaya**, featuring notices, gallery, academics, admissions, and results management.

## ✨ Features

- **🏫 School Information Management**: Dynamic school info, banners, and facilities
- **📢 Notices System**: Post and manage school notices and announcements
- **📸 Gallery**: Photo albums and gallery management with image uploads
- **📚 Academics**: Class and subject management
- **📝 Admissions**: Handle admission inquiries and applications
- **📊 Results**: Student examination results management
- **🎨 Beautiful Admin Panel**: Jazzmin-themed admin interface
- **📱 Responsive Design**: Mobile-friendly interface
- **☁️ Cloud Storage**: Cloudinary integration for media files
- **🔒 Secure**: Production-ready security settings

## 🛠️ Technology Stack

- **Framework**: Django 5.1.5
- **Database**: PostgreSQL (production) / SQLite (development)
- **Media Storage**: Cloudinary
- **Static Files**: WhiteNoise
- **Admin Theme**: Django Jazzmin
- **Server**: Gunicorn
- **Deployment**: Vercel / Railway / Render

## 📋 Prerequisites

- Python 3.11+
- pip (Python package manager)
- PostgreSQL (for production) or SQLite (for development)
- Cloudinary account (for media file storage)

## 🚀 Local Development Setup

### 1. Clone the Repository

\`\`\`bash
git clone <your-repo-url>
cd Vidya
\`\`\`

### 2. Create Virtual Environment

\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
\`\`\`

### 3. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Environment Configuration

Copy the example environment file and configure:

\`\`\`bash
cp .env.example .env
\`\`\`

Edit `.env` with your settings:
\`\`\`bash
SECRET_KEY=your-generated-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
# Leave DATABASE_URL empty to use SQLite for development
\`\`\`

Generate a secret key:
\`\`\`bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
\`\`\`

### 5. Database Setup

\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

### 6. Create Superuser

\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 7. Collect Static Files

\`\`\`bash
python manage.py collectstatic --noinput
\`\`\`

### 8. Run Development Server

\`\`\`bash
python manage.py runserver
\`\`\`

Visit:
- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## 🌐 Deployment

This project is configured for deployment on multiple platforms:

### Vercel (Recommended)
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed Vercel deployment instructions.

### Railway
Already configured with `railway.toml`. Connect your GitHub repo and deploy.

### Render
Already configured with `render.yaml`. Connect your GitHub repo and deploy.

## 📦 Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Generate using Django command |
| `DEBUG` | Debug mode (False in production) | `False` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `your-domain.vercel.app` |

### Database (Production)

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |

### Cloudinary (Media Files)

| Variable | Description |
|----------|-------------|
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | Your Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret |

## 📁 Project Structure

\`\`\`
Vidya/
├── api/                    # Vercel serverless entry point
│   └── index.py
├── config/                 # Django project configuration
│   ├── settings.py        # Main settings
│   ├── urls.py            # URL configuration
│   └── wsgi.py            # WSGI application
├── core/                   # Core app (home, about, contact)
├── notices/                # Notices management
├── gallery/                # Photo gallery
├── academics/              # Academic management
├── admissions/             # Admission inquiries
├── results/                # Student results
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── staticfiles/            # Collected static files
├── media/                  # User uploads (local dev only)
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── .env.example          # Environment variables template
└── README.md             # This file
\`\`\`

## 🔐 Security Notes

- Never commit `.env` file or expose `SECRET_KEY`
- Set `DEBUG=False` in production
- Use strong passwords for admin accounts
- Keep dependencies updated
- Use HTTPS in production (automatic on Vercel/Railway/Render)

## 📝 License

This project is for educational purposes for Vidya Bharti Awasiya Vidyalaya.

## 🤝 Support

For issues or questions, please contact the development team.

---

**Built with ❤️ for Vidya Bharti Awasiya Vidyalaya**
