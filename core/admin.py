from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, SchoolInfo, Facility


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('heading', 'preview_image', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('heading', 'subheading')
    ordering = ('order', '-created_at')
    
    fieldsets = (
        ('Banner Content', {
            'fields': ('heading', 'subheading', 'image')
        }),
        ('Settings', {
            'fields': ('is_active', 'order'),
            'classes': ('collapse',)
        }),
    )
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="60" style="object-fit: cover; border-radius: 4px;"/>', obj.image.url)
        return "-"
    preview_image.short_description = "Preview"


@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'email')
    
    fieldsets = (
        ('🏫 School Identity', {
            'fields': ('name', 'tagline', 'logo', 'established_year'),
            'description': 'Basic school information displayed on the website header and footer.'
        }),
        ('📞 Contact Information', {
            'fields': ('phone1', 'phone2', 'email', 'address'),
            'description': 'Contact details shown in the top bar and contact page.'
        }),
        ('📝 About Section', {
            'fields': ('about_text', 'mission', 'vision'),
            'description': 'Text content for the About Us page.',
            'classes': ('wide',)
        }),
    )
    
    def has_add_permission(self, request):
        if SchoolInfo.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'description')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Facility Details', {
            'fields': ('name', 'description', 'image')
        }),
        ('Display Settings', {
            'fields': ('icon', 'is_active', 'order'),
            'description': 'Icon should be a Font Awesome class (e.g., fa-book, fa-home)'
        }),
    )
    
    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<i class="fas {}"></i> {}', obj.icon, obj.icon)
        return "-"
    icon_preview.short_description = "Icon"
