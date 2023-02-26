from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('user_logout', views.user_logout, name='logout'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('homepage/', views.homepage, name='homepage'),
]
