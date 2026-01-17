from django.shortcuts import render, get_object_or_404
from .models import Album, GalleryImage


def gallery_view(request):
    """Display all albums with their cover images."""
    albums = Album.objects.filter(is_active=True)
    return render(request, 'gallery/gallery.html', {'albums': albums})


def album_detail_view(request, pk):
    """Display all images in an album."""
    album = get_object_or_404(Album, pk=pk, is_active=True)
    images = album.images.all()
    return render(request, 'gallery/album_detail.html', {'album': album, 'images': images})
