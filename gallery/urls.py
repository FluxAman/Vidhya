from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('album/<int:pk>/', views.album_detail_view, name='album_detail'),
]
