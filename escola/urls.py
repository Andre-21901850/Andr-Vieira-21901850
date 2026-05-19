from django.urls import path
from . import views

urlpatterns = [
    path('turmas/', views.turmas_view, name="turmas"),
    path('professores/', views.professores_view, name="professores"),
    path('alunos/', views.alunos_view, name="alunos"),
    path('', views.turmas_view),
]