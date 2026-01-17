from django.shortcuts import render, get_object_or_404
from .models import Notice


def notice_list_view(request):
    """List all active notices."""
    notices = Notice.objects.filter(is_active=True)
    return render(request, 'notices/notice_list.html', {'notices': notices})


def notice_detail_view(request, pk):
    """Detail view for a single notice."""
    notice = get_object_or_404(Notice, pk=pk, is_active=True)
    return render(request, 'notices/notice_detail.html', {'notice': notice})
