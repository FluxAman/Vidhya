# Vercel Deployment Checklist

Use this checklist when deploying to Vercel:

## Pre-Deployment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Test locally: `python3 manage.py runserver`
- [ ] Push code to GitHub
- [ ] Set up PostgreSQL database (Vercel Postgres/Neon/Supabase)
- [ ] Set up Cloudinary account (optional, for media files)

## Environment Variables (Set in Vercel Dashboard)
- [ ] `SECRET_KEY` - Generate new one
- [ ] `DEBUG` - Set to `False`
- [ ] `DATABASE_URL` - PostgreSQL connection string
- [ ] `CLOUDINARY_CLOUD_NAME` - From Cloudinary dashboard
- [ ] `CLOUDINARY_API_KEY` - From Cloudinary dashboard
- [ ] `CLOUDINARY_API_SECRET` - From Cloudinary dashboard

## Deploy
- [ ] Import project in Vercel dashboard
- [ ] Configure environment variables
- [ ] Deploy to production
- [ ] Wait for build completion

## Post-Deployment
- [ ] Run migrations on production database
- [ ] Create superuser account
- [ ] Test site: `https://your-project.vercel.app`
- [ ] Test admin: `https://your-project.vercel.app/admin`
- [ ] Test health check: `https://your-project.vercel.app/health/`

## Optional
- [ ] Configure custom domain
- [ ] Set up monitoring
- [ ] Configure backups for database

---

**For detailed instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)**
