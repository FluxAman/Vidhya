from .models import SchoolInfo


def school_info(request):
    """
    Injects school_info into every template context globally.
    This eliminates repeated DB queries across individual views.
    """
    return {
        'school_info': SchoolInfo.objects.first(),
    }
