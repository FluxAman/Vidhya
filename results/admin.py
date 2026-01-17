from django.contrib import admin
from django.utils.html import format_html
from .models import ExamResult


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'academic_class', 'exam_type', 'academic_year', 'published_date', 'is_active', 'download_link')
    list_filter = ('academic_class', 'exam_type', 'academic_year', 'is_active', 'published_date')
    list_editable = ('is_active',)
    search_fields = ('exam_name', 'description')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    list_per_page = 20
    
    fieldsets = (
        ('📝 Exam Details', {
            'fields': ('exam_name', 'exam_type', 'academic_year'),
            'description': 'Enter the exam name and select exam type.'
        }),
        ('📚 Class & Result', {
            'fields': ('academic_class', 'result_pdf'),
            'description': 'Select the class and upload the result PDF file.'
        }),
        ('📋 Additional Info', {
            'fields': ('description', 'is_active'),
            'classes': ('collapse',)
        }),
    )
    
    def download_link(self, obj):
        if obj.result_pdf:
            return format_html(
                '<a href="{}" target="_blank" style="background: #28a745; color: white; padding: 5px 12px; border-radius: 4px; text-decoration: none;"><i class="fas fa-download"></i> Download PDF</a>',
                obj.result_pdf.url
            )
        return "-"
    download_link.short_description = "PDF"
