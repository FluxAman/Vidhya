from django import forms
from .models import AdmissionInquiry


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionInquiry
        fields = [
            'student_name', 'date_of_birth', 'gender', 'applying_for_class', 'previous_school',
            'father_name', 'mother_name', 'guardian_phone', 'alternate_phone', 'email',
            'address', 'message'
        ]
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student full name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'applying_for_class': forms.Select(attrs={'class': 'form-control'}),
            'previous_school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Previous school name (optional)'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Father's full name"}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mother's full name"}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit mobile number'}),
            'alternate_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternate number (optional)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address (optional)'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Full residential address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Any message or query (optional)'}),
        }
