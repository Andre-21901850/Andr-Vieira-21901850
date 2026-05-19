from django.shortcuts import render
from .models import Turma, Professor, Aluno

def turmas_view(request):
    turmas = Turma.objects.prefetch_related('alunos').all()
    return render(request, 'escola/turmas.html', {'turmas': turmas})

def professores_view(request):
    professores = Professor.objects.select_related('turma').all()
    return render(request, 'escola/professores.html', {'professores': professores})

def alunos_view(request):
    alunos = Aluno.objects.select_related('turma').all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})