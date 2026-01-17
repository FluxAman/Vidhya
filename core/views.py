from django.shortcuts import render
from .models import Banner, SchoolInfo, Facility
from notices.models import Notice


def home_view(request):
    """Home page with banners, latest notices, and school intro."""
    banners = Banner.objects.filter(is_active=True)
    latest_notices = Notice.objects.filter(is_active=True)[:5]
    school_info = SchoolInfo.objects.first()
    
    context = {
        'banners': banners,
        'banner_list': banners,  # Renamed to avoid potential conflict with built-ins if any
        'banners': banners,
        'latest_notices': latest_notices,
        'facilities': Facility.objects.filter(is_active=True).order_by('order'),
        'school_info': school_info,
    }
    return render(request, 'core/home.html', context)


def about_view(request):
    """About page with school information."""
    school_info = SchoolInfo.objects.first()
    return render(request, 'core/about.html', {'school_info': school_info})


def contact_view(request):
    """Contact page with school contact details."""
    school_info = SchoolInfo.objects.first()
    return render(request, 'core/contact.html', {'school_info': school_info})


def facilities_view(request):
    """Page displaying all school facilities."""
    facilities = Facility.objects.filter(is_active=True)
    return render(request, 'core/facilities.html', {'facilities': facilities})
