# Deploying to Vercel - Complete Guide

This guide walks you through deploying the Vidya Bharti school management system to Vercel.

## 📋 Prerequisites

Before you begin, ensure you have:

- ✅ A [Vercel account](https://vercel.com/signup) (free tier works fine)
- ✅ A [GitHub account](https://github.com) with your code pushed
- ✅ A PostgreSQL database (see Database Setup below)
- ✅ A [Cloudinary account](https://cloudinary.com/users/register/free) for media files (optional but recommended)

## 🗄️ Database Setup

Vercel doesn't include a built-in database, so you'll need to set one up. Here are your options:

### Option 1: Vercel Postgres (Recommended)

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Storage** → **Create Database**
3. Select **Postgres**
4. Choose a name and region (select one close to your users)
5. After creation, copy the `DATABASE_URL` connection string

### Option 2: Neon (Free PostgreSQL)

1. Sign up at [Neon](https://neon.tech)
2. Create a new project
3. Copy the connection string from the dashboard
4. It should look like: `postgresql://user:pass@host.region.neon.tech/dbname`

### Option 3: Supabase (Free PostgreSQL)

1. Sign up at [Supabase](https://supabase.com)
2. Create a new project
3. Go to **Settings** → **Database**
4. Copy the **Connection string** (URI format)

## ☁️ Cloudinary Setup (Media Files)

Since Vercel has a read-only filesystem, you need Cloudinary for user-uploaded images:

1. Sign up at [Cloudinary](https://cloudinary.com/users/register/free)
2. Go to your [Dashboard](https://cloudinary.com/console)
3. Note down these values:
   - **Cloud Name**
   - **API Key**
   - **API Secret**

## 🚀 Deployment Steps

### Method 1: Deploy via Vercel Dashboard (Easiest)

#### 1. Push Code to GitHub

Make sure your latest code is on GitHub:

\`\`\`bash
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
\`\`\`

#### 2. Import Project to Vercel

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Add New** → **Project**
3. Import your GitHub repository
4. Select the repository and click **Import**

#### 3. Configure Environment Variables

Before deploying, add these environment variables in Vercel:

**Required Variables:**

| Name | Value | Where to Get |
|------|-------|--------------|
| `SECRET_KEY` | Generate new secret key | Use command below |
| `DEBUG` | `False` | Always False in production |
| `ALLOWED_HOSTS` | Leave empty (auto-configured) | Vercel sets this |
| `DATABASE_URL` | Your PostgreSQL URL | From database setup above |

**For Media Files (Cloudinary):**

| Name | Value | Where to Get |
|------|-------|--------------|
| `CLOUDINARY_CLOUD_NAME` | Your cloud name | Cloudinary Dashboard |
| `CLOUDINARY_API_KEY` | Your API key | Cloudinary Dashboard |
| `CLOUDINARY_API_SECRET` | Your API secret | Cloudinary Dashboard |

**Generate SECRET_KEY:**
\`\`\`bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
\`\`\`

#### 4. Deploy

1. Click **Deploy**
2. Wait for the build to complete (2-3 minutes)
3. Once deployed, you'll get a URL like `https://your-project.vercel.app`

### Method 2: Deploy via Vercel CLI

#### 1. Install Vercel CLI

\`\`\`bash
npm install -g vercel
\`\`\`

#### 2. Login to Vercel

\`\`\`bash
vercel login
\`\`\`

#### 3. Deploy

\`\`\`bash
cd /Users/amankumar/Coding/Vidya
vercel
\`\`\`

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Choose your account
- Link to existing project? **N** (first time)
- What's your project's name? Enter a name
- In which directory is your code located? **. /** (current directory)

#### 4. Add Environment Variables

\`\`\`bash
# Add each variable
vercel env add SECRET_KEY
vercel env add DATABASE_URL
vercel env add CLOUDINARY_CLOUD_NAME
vercel env add CLOUDINARY_API_KEY
vercel env add CLOUDINARY_API_SECRET

# Select "Production" for all
\`\`\`

#### 5. Deploy to Production

\`\`\`bash
vercel --prod
\`\`\`

## 🔧 Post-Deployment Setup

### 1. Run Database Migrations

After your first deployment, you need to run migrations. There are two ways:

**Option A: Using Vercel CLI**
\`\`\`bash
vercel env pull .env.production
python manage.py migrate --settings=config.settings
\`\`\`

**Option B: Via Python Shell on Vercel**

Create a temporary file `migrate.py` in your project:
\`\`\`python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.core.management import call_command
call_command('migrate')
\`\`\`

Then access it via: `https://your-project.vercel.app/migrate/` (you'll need to create a view for this)

**Best Practice**: Connect to your PostgreSQL database directly and run migrations locally:

\`\`\`bash
# Set DATABASE_URL to your production database
export DATABASE_URL="your-production-database-url"
python manage.py migrate
\`\`\`

### 2. Create Superuser

Connect to your production database and create an admin user:

\`\`\`bash
export DATABASE_URL="your-production-database-url"
python manage.py createsuperuser
\`\`\`

### 3. Access Your Site

- **Website**: `https://your-project.vercel.app`
- **Admin Panel**: `https://your-project.vercel.app/admin`
- **Health Check**: `https://your-project.vercel.app/health/`

## 🔍 Troubleshooting

### Build Fails

**Error**: `Module not found: cloudinary`
**Solution**: Make sure `requirements.txt` is in the root directory

**Error**: `SECRET_KEY not set`
**Solution**: Add `SECRET_KEY` environment variable in Vercel dashboard

### Runtime Errors

**Error**: `DisallowedHost at /`
**Solution**: Vercel automatically adds your domain to `ALLOWED_HOSTS`. If you added a custom domain, add it to the environment variable:
\`\`\`bash
ALLOWED_HOSTS=your-custom-domain.com,your-project.vercel.app
\`\`\`

**Error**: `Could not connect to database`
**Solution**: 
- Verify `DATABASE_URL` is correctly set
- Check your database is accessible (not behind a firewall)
- Ensure connection string format is correct

### Static Files Not Loading

**Issue**: CSS/JS files return 404

**Solution**: 
1. Check `vercel.json` routes are correct
2. Run `python manage.py collectstatic` locally to verify it works
3. Check Vercel build logs for errors

### Media Files Not Uploading

**Issue**: Images can't be uploaded

**Solution**:
- Ensure Cloudinary environment variables are set
- Check Cloudinary dashboard for API usage
- Verify `CLOUDINARY_CONFIGURED` is True in your Django logs

## 📊 Monitoring

### View Logs

**Vercel Dashboard:**
1. Go to your project
2. Click **Deployments**
3. Click on a deployment
4. Click **View Function Logs**

**Vercel CLI:**
\`\`\`bash
vercel logs
\`\`\`

### Check Health

Visit: `https://your-project.vercel.app/health/`

Should return: `{"status": "healthy"}`

## 🔄 Updating Your Deployment

Every time you push to GitHub, Vercel automatically deploys!

\`\`\`bash
git add .
git commit -m "Update feature"
git push origin main
\`\`\`

Vercel will:
- Detect the push
- Build your project
- Deploy automatically
- Send you a deployment notification

## 🌐 Custom Domain

### Add Custom Domain

1. Go to project **Settings** → **Domains**
2. Click **Add Domain**
3. Enter your domain name
4. Follow DNS configuration instructions
5. Update `ALLOWED_HOSTS` environment variable:
   \`\`\`
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   \`\`\`

## ⚡ Performance Tips

1. **Enable Caching**: Vercel automatically caches static files
2. **Use CDN**: Static files are served via Vercel's global CDN
3. **Database Connection Pooling**: Already configured in settings
4. **Optimize Images**: Cloudinary automatically optimizes images

## 🔒 Security Checklist

- ✅ `DEBUG=False` in production
- ✅ Strong `SECRET_KEY` (never reuse development key)
- ✅ Database credentials secured in environment variables
- ✅ HTTPS enabled (automatic on Vercel)
- ✅ CSRF protection enabled
- ✅ Secure cookies enabled for non-DEBUG mode

## 📞 Support

### Vercel Support
- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Discord](https://vercel.com/discord)
- [Vercel Support](https://vercel.com/support)

### Django Deployment
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/)
- Run: `python manage.py check --deploy`

---

**Deployed Successfully? 🎉**

You now have a professional, production-ready school management system running on Vercel!
