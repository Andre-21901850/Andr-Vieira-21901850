from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
]