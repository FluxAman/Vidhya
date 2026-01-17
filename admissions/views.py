from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionForm


def admission_page(request):
    """Display admission information and form."""
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your admission inquiry has been submitted successfully! We will contact you soon.')
            return redirect('admissions:admission')
    else:
        form = AdmissionForm()
    
    return render(request, 'admissions/admission.html', {'form': form})
