from django.shortcuts import render
from .models import Tecnologia, Projeto, UnidadeCurricular, TFC, Competencia, Licenciatura

def index_view(request):
    licenciatura = Licenciatura.objects.first()
    return render(request, 'portfolio/index.html', {'licenciatura': licenciatura})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def projetos_view(request):
    projetos = Projeto.objects.prefetch_related('tecnologias').select_related('uc').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.prefetch_related('docentes').select_related('licenciatura').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})