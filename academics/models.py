from django.db import models


class AcademicClass(models.Model):
    """Academic classes (Grade 1, Grade 2, etc.)."""
    name = models.CharField(max_length=50)  # e.g., "Class 1", "Class 10"
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text='Order of display')

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Subjects taught in each class."""
    name = models.CharField(max_length=100)
    academic_class = models.ForeignKey(
        AcademicClass, 
        on_delete=models.CASCADE, 
        related_name='subjects'
    )
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.academic_class.name})'
