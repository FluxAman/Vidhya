from django.contrib import admin
from django.utils.html import format_html
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'status_badge', 'is_important', 'has_attachment')
    list_filter = ('is_active', 'is_important', 'date_posted')
    list_editable = ('is_important',)
    search_fields = ('title', 'content')
    date_hierarchy = 'date_posted'
    ordering = ('-date_posted',)
    
    fieldsets = (
        ('📢 Notice Content', {
            'fields': ('title', 'content'),
            'description': 'Enter the notice title and detailed content.'
        }),
        ('📎 Attachment', {
            'fields': ('attachment',),
            'description': 'Upload PDF or document file if needed.',
            'classes': ('collapse',)
        }),
        ('⚙️ Settings', {
            'fields': ('date_posted', 'is_active', 'is_important'),
            'description': 'Control visibility and importance of this notice.'
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
