from django.db import models


class Album(models.Model):
    """Photo albums to organize gallery images."""
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='gallery/covers/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def image_count(self):
        return self.images.count()


class GalleryImage(models.Model):
    """Individual images in the gallery."""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or f'Image {self.pk}'
