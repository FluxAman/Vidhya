from django.contrib import admin
from django.utils.html import format_html
from .models import Album, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    fields = ('image', 'title', 'preview')
    readonly_fields = ('preview',)
    
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit: cover; border-radius: 4px;"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_preview', 'image_count', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description')
    ordering = ('order', '-created_at')
    inlines = [GalleryImageInline]
    
    fieldsets = (
        ('📸 Album Details', {
            'fields': ('title', 'description', 'cover_image'),
            'description': 'Create a photo album with a title and cover image.'
        }),
        ('⚙️ Settings', {
            'fields': ('is_active', 'order'),
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
    list_display = ('title', 'preview', 'album', 'uploaded_at')
    list_filter = ('album', 'uploaded_at')
    search_fields = ('title', 'album__title')
    ordering = ('-uploaded_at',)
    
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit: cover; border-radius: 4px;"/>', obj.image.url)
        return "-"
    preview.short_description = "Preview"
