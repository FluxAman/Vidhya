from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import Notice


class NoticeAdminForm(forms.ModelForm):
    """Custom form for Notice with better widgets."""
    class Meta:
        model = Notice
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 12, 'cols': 100, 'style': 'width: 100%;'}),
        }


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    """Admin interface for managing school notices."""
    form = NoticeAdminForm
    list_display = ('title', 'date_posted', 'status_badge', 'is_important', 'has_attachment')
    list_filter = ('is_active', 'is_important', 'date_posted')
    list_editable = ('is_important',)
    search_fields = ('title', 'content')
    date_hierarchy = 'date_posted'
    ordering = ('-date_posted',)
    
    fieldsets = (
        ('📢 Notice Details', {
            'fields': ('title', 'content'),
            'description': 'Enter notice title and detailed content.'
        }),
        ('📅 Date & Time', {
            'fields': ('date_posted',),
            'description': 'Notice date - leave empty for current date/time or set custom date',
        }),
        ('📎 Attachment (Optional)', {
            'fields': ('attachment',),
            'description': 'Upload PDF or document file (e.g., exam schedule, circular)',
            'classes': ('collapse',)
        }),
        ('⚙️ Display Settings', {
            'fields': ('is_active', 'is_important'),
            'description': 'is_active: Show on website | is_important: Highlight notice'
        }),
    )
    
    def status_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="background: #28a745; color: white; padding: 3px 10px; border-radius: 12px; font-size: 11px;">Active</span>')
        return format_html('<span style="background: #dc3545; color: white; padding: 3px 10px; border-radius: 12px; font-size: 11px;">Inactive</span>')
    status_badge.short_description = "Status"
    
    def has_attachment(self, obj):
        if obj.attachment:
            return format_html('<i class="fas fa-paperclip" style="color: #007bff;"></i> Yes')
        return "-"
    has_attachment.short_description = "File"
