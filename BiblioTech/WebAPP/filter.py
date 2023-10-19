import django_filters
from API.models import *
from django import forms

class AutoresFiltro(django_filters.FilterSet):
    class Meta:
        model = Autor
        fields = '__all__'

class EditoraFiltro(django_filters.FilterSet):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroFiltro(django_filters.FilterSet):
    class Meta:
        model = Livro
        fields = '__all__'

class GeneroLivroFiltro(django_filters.FilterSet):
    class Meta:
        model = GeneroLivro
        fields = '__all__'

class CursoFiltro(django_filters.FilterSet):
    class Meta:
        model = Curso
        fields = '__all__'

class AlunoFiltro(django_filters.FilterSet):
    class Meta:
        model = Aluno
        fields = '__all__'

class EmprestimoFiltro(django_filters.FilterSet):
    class Meta:
        model = Emprestimo
        fields = '__all__'

class DevolucaoFiltro(django_filters.FilterSet):
    class Meta:
        model = Devolucao
        fields = '__all__'

class DetalhesLivroFiltro(django_filters.FilterSet):
    class Meta:
        model = DetalhesLivro
        fields = '__all__'