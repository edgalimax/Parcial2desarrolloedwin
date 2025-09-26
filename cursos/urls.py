from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # http://127.0.0.1:8000/
    path('home/', views.home, name='home_alt'),  # http://127.0.0.1:8000/home
    path('videos/', views.videos_list, name='videos_list'),
    path('videos/nuevo/', views.video_create, name='video_create'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/nuevo/', views.usuario_create, name='usuario_create'),
    path('creditos/', views.creditos, name='creditos'),
]
