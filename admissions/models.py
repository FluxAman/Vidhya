from django.db import models


class AdmissionInquiry(models.Model):
    """Store admission form submissions."""
    
    CLASS_CHOICES = [
        ('nursery', 'Nursery'),
        ('lkg', 'LKG'),
        ('ukg', 'UKG'),
        ('class1', 'Class 1'),
        ('class2', 'Class 2'),
        ('class3', 'Class 3'),
        ('class4', 'Class 4'),
        ('class5', 'Class 5'),
        ('class6', 'Class 6'),
        ('class7', 'Class 7'),
        ('class8', 'Class 8'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('contacted', 'Contacted'),
        ('enrolled', 'Enrolled'),
        ('rejected', 'Rejected'),
    ]
    
    # Student Information
    student_name = models.CharField(max_length=100, verbose_name="Student's Full Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    applying_for_class = models.CharField(max_length=20, choices=CLASS_CHOICES, verbose_name="Applying for Class")
    previous_school = models.CharField(max_length=200, blank=True, verbose_name="Previous School (if any)")
    
    # Parent/Guardian Information
    father_name = models.CharField(max_length=100, verbose_name="Father's Name")
    mother_name = models.CharField(max_length=100, verbose_name="Mother's Name")
    guardian_phone = models.CharField(max_length=15, verbose_name="Contact Number")
    alternate_phone = models.CharField(max_length=15, blank=True, verbose_name="Alternate Number")
    email = models.EmailField(blank=True, verbose_name="Email Address")
    address = models.TextField(verbose_name="Residential Address")
    
    # Additional Info
    message = models.TextField(blank=True, verbose_name="Any Message/Query")
    
    # System fields
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, verbose_name="Admin Notes")
    
    class Meta:
        verbose_name = "Admission Inquiry"
        verbose_name_plural = "Admission Inquiries"
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.student_name} - {self.get_applying_for_class_display()}"
