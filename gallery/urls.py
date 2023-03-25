from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:car_id>/detail/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
]
