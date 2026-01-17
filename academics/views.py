from django.shortcuts import render
from .models import AcademicClass


def academics_view(request):
    """Display all academic classes with their subjects."""
    classes = AcademicClass.objects.prefetch_related('subjects').all()
    return render(request, 'academics/academics.html', {'classes': classes})
