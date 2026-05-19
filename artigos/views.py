from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

def artigos_view(request):
    artigos = Artigo.objects.prefetch_related('comentarios', 'likes').select_related('autor').order_by('-data_criacao')
    return render(request, 'artigos/artigos.html', {'artigos': artigos})

@login_required
def artigo_criar(request):
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Novo Artigo'})

@login_required
def artigo_editar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Editar Artigo'})

@login_required
def artigo_like(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos')

@login_required
def comentario_criar(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        comentario.autor = request.user
        comentario.save()
        return redirect('artigos')
    return redirect('artigos')