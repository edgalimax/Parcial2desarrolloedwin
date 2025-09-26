from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Video, Usuario
from .forms import VideoForm, UsuarioForm

def home(request):
    return render(request, 'cursos/home.html')

def videos_list(request):
    videos = Video.objects.all()
    return render(request, 'cursos/videos_list.html', {'videos': videos})

def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video agregado correctamente.')
            return redirect('videos_list')
    else:
        form = VideoForm()
    return render(request, 'cursos/video_form.html', {'form': form})

def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'cursos/usuarios_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('usuarios_list')
    else:
        form = UsuarioForm()
    return render(request, 'cursos/usuario_form.html', {'form': form})

def creditos(request):
    return render(request, 'cursos/creditos.html')
