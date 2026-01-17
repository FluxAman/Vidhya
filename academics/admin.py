from django.contrib import admin
from .models import AcademicClass, Subject


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 5
    fields = ('name', 'description')


@admin.register(AcademicClass)
class AcademicClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_count', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    ordering = ('order', 'name')
    inlines = [SubjectInline]
    
    fieldsets = (
        ('📚 Class Details', {
            'fields': ('name', 'description', 'order'),
            'description': 'Add classes from Nursery to Class 8. Use order to arrange display sequence.'
        }),
    )
    
    def subject_count(self, obj):
        count = obj.subjects.count()
        return f"{count} subjects"
    subject_count.short_description = "Subjects"


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_class')
    list_filter = ('academic_class',)
    search_fields = ('name', 'academic_class__name')
    ordering = ('academic_class__order', 'name')
