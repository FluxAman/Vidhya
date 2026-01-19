from django.contrib import admin
from django.utils.html import format_html
from .models import Album, GalleryImage


class GalleryImageInline(admin.TabularInline):
    """Inline form to add multiple images to an album at once."""
    model = GalleryImage
    extra = 5  # Show 5 empty slots for new images
    fields = ('image', 'title', 'preview')
    readonly_fields = ('preview',)
    verbose_name = "Gallery Image"
    verbose_name_plural = "📷 Gallery Images (Upload Multiple)"
    
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit: cover; border-radius: 4px;"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Admin interface for managing photo albums."""
    list_display = ('title', 'cover_preview', 'image_count', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description')
    ordering = ('order', '-created_at')
    inlines = [GalleryImageInline]
    
    fieldsets = (
        ('📸 Album Information', {
            'fields': ('title', 'description', 'cover_image'),
            'description': 'Create album and upload multiple images at once. Cover image is optional.'
        }),
        ('⚙️ Display Settings', {
            'fields': ('is_active', 'order'),
            'description': 'Control visibility and order on website.',
            'classes': ('collapse',)
        }),
    )
    
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit: cover; border-radius: 4px;"/>', obj.cover_image.url)
        return "-"
    cover_preview.short_description = "Cover"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """Admin interface for individual gallery images."""
    list_display = ('title', 'preview', 'album', 'uploaded_at')
    list_filter = ('album', 'uploaded_at')
    search_fields = ('title', 'album__title')
    ordering = ('-uploaded_at',)
    
    fieldsets = (
        ('📷 Image Upload', {
            'fields': ('album', 'image', 'title'),
            'description': 'Upload single image. Tip: Use Albums to upload multiple images at once!'
        }),
    )
    
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit: cover; border-radius: 4px;"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"
