from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnologia, Projeto, UnidadeCurricular, TFC, Competencia, Licenciatura, Formacao
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

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

# CRUD Projeto
def projeto_criar(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Novo Projeto'})

def projeto_editar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto'})

def projeto_apagar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_confirmar_apagar.html', {'objeto': projeto})

# CRUD Tecnologia
def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

def tecnologia_editar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Tecnologia'})

def tecnologia_apagar(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': tecnologia})

# CRUD Competencia
def competencia_criar(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Competência'})

def competencia_editar(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Competência'})

def competencia_apagar(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': competencia})

# CRUD Formacao
def formacao_criar(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Formação'})

def formacao_editar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Formação'})

def formacao_apagar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': formacao})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})