"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('notices/', include('notices.urls')),
    path('gallery/', include('gallery.urls')),
    path('academics/', include('academics.urls')),
    path('admission/', include('admissions.urls')),
    path('results/', include('results.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
