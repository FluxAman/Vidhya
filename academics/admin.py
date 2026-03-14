from django.contrib import admin
from .models import AcademicClass, Subject, Student


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 5
    fields = ('name', 'description')


class StudentInline(admin.TabularInline):
    model = Student
    extra = 10
    fields = ('roll_number', 'full_name', 'father_name', 'phone', 'admission_date', 'is_active')
    readonly_fields = ('roll_number',)
    ordering = ('roll_number',)


@admin.register(AcademicClass)
class AcademicClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_count', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    ordering = ('order', 'name')
    inlines = [SubjectInline, StudentInline]

    fieldsets = (
        ('📚 Class Details', {
            'fields': ('name', 'description', 'order'),
            'description': 'Add classes from Nursery to Class 8. Use order to arrange display sequence.'
        }),
    )

    def student_count(self, obj):
        count = obj.students.count()
        return f"{count} students"
    student_count.short_description = "Students"


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_class')
    list_filter = ('academic_class',)
    search_fields = ('name', 'academic_class__name')
    ordering = ('academic_class__order', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'academic_class', 'roll_number', 'father_name', 'phone', 'admission_date', 'is_active')
    list_filter = ('academic_class', 'is_active', 'admission_date')
    search_fields = ('full_name', 'father_name', 'phone', 'address', 'academic_class__name')
    ordering = ('academic_class__order', 'academic_class__name', 'roll_number')
    list_per_page = 50
