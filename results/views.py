from django.shortcuts import render
from .models import ExamResult


def results_page(request):
    """Display exam results grouped by class."""
    results = ExamResult.objects.filter(is_active=True).order_by('academic_class', '-published_date')
    
    # Group results by class
    results_by_class = {}
    for result in results:
        class_name = result.get_academic_class_display()
        if class_name not in results_by_class:
            results_by_class[class_name] = []
        results_by_class[class_name].append(result)
    
    return render(request, 'results/results.html', {
        'results_by_class': results_by_class,
    })
