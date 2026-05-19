from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'tecnologias', 'uc', 'imagem', 'link_github', 'link_demo', 'conceitos_aplicados', 'data']

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'descricao', 'logo', 'link_website', 'nivel_interesse', 'categoria']

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'descricao', 'nivel', 'tecnologias', 'projetos']

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome', 'instituicao', 'descricao', 'data_inicio', 'data_fim', 'certificado', 'link']