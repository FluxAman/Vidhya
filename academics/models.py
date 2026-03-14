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


class Student(models.Model):
    """Individual student enrolled in a class (admin only)."""
    academic_class = models.ForeignKey(
        AcademicClass,
        on_delete=models.PROTECT,
        related_name='students',
        verbose_name='Class',
    )
    full_name = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    admission_date = models.DateField()
    roll_number = models.PositiveIntegerField(
        help_text='Roll number within the class',
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True, help_text='Currently studying in this school')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['academic_class__order', 'academic_class__name', 'roll_number']
        unique_together = ('academic_class', 'roll_number')
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.full_name} ({self.academic_class.name})"

    def save(self, *args, **kwargs):
        # Auto-assign next roll number within the class if not set
        if self.roll_number is None and self.academic_class_id:
            last_roll = (
                Student.objects
                .filter(academic_class_id=self.academic_class_id)
                .order_by('-roll_number')
                .values_list('roll_number', flat=True)
                .first()
            )
            self.roll_number = (last_roll or 0) + 1
        super().save(*args, **kwargs)
