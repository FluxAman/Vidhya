from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.notice_list_view, name='list'),
    path('<int:pk>/', views.notice_detail_view, name='detail'),
]
