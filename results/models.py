from django.db import models


class ExamResult(models.Model):
    """Store exam results with PDF uploads for each class."""
    
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
    
    EXAM_TYPE_CHOICES = [
        ('unit_test_1', 'Unit Test 1'),
        ('unit_test_2', 'Unit Test 2'),
        ('half_yearly', 'Half Yearly Exam'),
        ('unit_test_3', 'Unit Test 3'),
        ('unit_test_4', 'Unit Test 4'),
        ('annual', 'Annual Exam'),
        ('other', 'Other'),
    ]
    
    exam_name = models.CharField(max_length=200, verbose_name="Exam Name")
    exam_type = models.CharField(max_length=50, choices=EXAM_TYPE_CHOICES, default='other')
    academic_class = models.CharField(max_length=20, choices=CLASS_CHOICES, verbose_name="Class")
    result_pdf = models.FileField(upload_to='results/', verbose_name="Result PDF")
    academic_year = models.CharField(max_length=20, default='2025-26', verbose_name="Academic Year")
    published_date = models.DateField(auto_now_add=True, verbose_name="Published Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    description = models.TextField(blank=True, verbose_name="Description/Notes")
    
    class Meta:
        verbose_name = "Exam Result"
        verbose_name_plural = "Exam Results"
        ordering = ['-published_date', 'academic_class']
    
    def __str__(self):
        return f"{self.exam_name} - {self.get_academic_class_display()} ({self.academic_year})"
