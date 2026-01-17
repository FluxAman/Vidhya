from django.contrib import admin
from django.utils.html import format_html
from .models import AdmissionInquiry


@admin.register(AdmissionInquiry)
class AdmissionInquiryAdmin(admin.ModelAdmin):
    # List view - shows only essential info
    list_display = ('student_name', 'guardian_phone', 'submitted_at', 'status_badge', 'view_details_link')
    list_filter = ('status', 'applying_for_class', 'submitted_at')
    search_fields = ('student_name', 'father_name', 'guardian_phone')
    date_hierarchy = 'submitted_at'
    ordering = ('-submitted_at',)
    list_per_page = 25
    
    # Hide these from list - only show when viewing details
    readonly_fields = ('submitted_at', 'student_info_display', 'parent_info_display', 'additional_info_display')
    
    # Organized fieldsets for detail view
    fieldsets = (
        ('📋 Student Information', {
            'fields': ('student_info_display',),
            'classes': ('wide',)
        }),
        ('👨‍👩‍👧 Parent/Guardian Information', {
            'fields': ('parent_info_display',),
            'classes': ('wide',)
        }),
        ('💬 Additional Information', {
            'fields': ('additional_info_display',),
            'classes': ('wide',)
        }),
        ('⚙️ Status & Admin Notes', {
            'fields': ('status', 'notes'),
            'description': 'Update the status and add any internal notes here.'
        }),
    )
    
    def view_details_link(self, obj):
        return format_html('<a href="{}/change/" style="background: #0b4585; color: white; padding: 5px 15px; border-radius: 4px; text-decoration: none;"><i class="fas fa-eye"></i> View Details</a>', obj.pk)
    view_details_link.short_description = "Action"
    
    def status_badge(self, obj):
        colors = {
            'pending': '#ffc107',
            'reviewed': '#17a2b8',
            'contacted': '#6f42c1',
            'enrolled': '#28a745',
            'rejected': '#dc3545',
        }
        color = colors.get(obj.status, '#6c757d')
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 12px; border-radius: 15px; font-size: 11px; font-weight: 500;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = "Status"
    
    def student_info_display(self, obj):
        return format_html('''
            <table style="width: 100%; border-collapse: collapse; background: #f8f9fa; border-radius: 8px;">
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; width: 200px; color: #495057;">Student Name</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Date of Birth</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Gender</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Applying for Class</td>
                    <td style="padding: 12px 15px; color: #212529;"><span style="background: #0b4585; color: white; padding: 3px 10px; border-radius: 4px;">{}</span></td>
                </tr>
                <tr>
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Previous School</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
            </table>
        ''', obj.student_name, obj.date_of_birth.strftime('%d %B %Y'), obj.get_gender_display(), obj.get_applying_for_class_display(), obj.previous_school or '-')
    student_info_display.short_description = ""
    
    def parent_info_display(self, obj):
        return format_html('''
            <table style="width: 100%; border-collapse: collapse; background: #f8f9fa; border-radius: 8px;">
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; width: 200px; color: #495057;">Father's Name</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Mother's Name</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Contact Number</td>
                    <td style="padding: 12px 15px; color: #212529;"><a href="tel:{}" style="color: #0b4585; font-weight: 600;"><i class="fas fa-phone"></i> {}</a></td>
                </tr>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Alternate Number</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Email</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr>
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Address</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
            </table>
        ''', obj.father_name, obj.mother_name, obj.guardian_phone, obj.guardian_phone, obj.alternate_phone or '-', obj.email or '-', obj.address)
    parent_info_display.short_description = ""
    
    def additional_info_display(self, obj):
        return format_html('''
            <table style="width: 100%; border-collapse: collapse; background: #f8f9fa; border-radius: 8px;">
                <tr style="border-bottom: 1px solid #dee2e6;">
                    <td style="padding: 12px 15px; font-weight: 600; width: 200px; color: #495057;">Message/Query</td>
                    <td style="padding: 12px 15px; color: #212529;">{}</td>
                </tr>
                <tr>
                    <td style="padding: 12px 15px; font-weight: 600; color: #495057;">Submitted On</td>
                    <td style="padding: 12px 15px; color: #212529;"><span style="background: #28a745; color: white; padding: 3px 10px; border-radius: 4px;">{}</span></td>
                </tr>
            </table>
        ''', obj.message or '-', obj.submitted_at.strftime('%d %B %Y at %I:%M %p'))
    additional_info_display.short_description = ""
    
    # Bulk actions
    actions = ['mark_as_reviewed', 'mark_as_contacted', 'mark_as_enrolled']
    
    def mark_as_reviewed(self, request, queryset):
        queryset.update(status='reviewed')
        self.message_user(request, f"{queryset.count()} inquiries marked as Reviewed.")
    mark_as_reviewed.short_description = "✓ Mark as Reviewed"
    
    def mark_as_contacted(self, request, queryset):
        queryset.update(status='contacted')
        self.message_user(request, f"{queryset.count()} inquiries marked as Contacted.")
    mark_as_contacted.short_description = "📞 Mark as Contacted"
    
    def mark_as_enrolled(self, request, queryset):
        queryset.update(status='enrolled')
        self.message_user(request, f"{queryset.count()} inquiries marked as Enrolled.")
    mark_as_enrolled.short_description = "🎓 Mark as Enrolled"
