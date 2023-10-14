from django.urls import path
from .views import *

app_name = 'API'

urlpatterns = [
    path('', routesList, name='routes-list'),
    # Autor
    path('autores/', AutoresView.as_view(), name='autor-list'),
    path('autor/<int:pk>/', AutorView.as_view(), name='autor-detail'),

    # Editora
    path('editoras/', EditorasView.as_view(), name='Editora-list'),
    path('editora/<int:pk>/', EditoraView.as_view(), name='Editora-detail'),

    # Livro
    path('livros/', LivrosView.as_view(), name='livro-list'),
    path('livro/<int:pk>/', LivroView.as_view(), name='livro-detail'),

    # GeneroLivro
    path('generolivros/', GeneroLivrosView.as_view(), name='generolivro-list'),
    path('generolivro/<int:pk>/', GeneroLivroView.as_view(), name='generolivro-detail'),

    # Usuario
    path('alunos/', AlunosView.as_view(), name='alunos'),
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),

    # Emprestimo
    path('emprestimos/', EmprestimosView.as_view(), name='emprestimo-list'),
    path('emprestimo/<int:pk>/', EmprestimoView.as_view(), name='emprestimo-detail'),

    # Devolucao
    path('devolucoes/', DevolucoesView.as_view(), name='devolucao-list'),
    path('devolucao/<int:pk>/', DevolucaoView.as_view(), name='devolucao-detail'),

    # DetalhesLivro
    path('detalheslivros/', DetalhesLivrosView.as_view(), name='detalheslivro-list'),
    path('detalheslivro/<int:pk>/', DetalhesLivrosView.as_view(), name='detalheslivro-detail'),

    # Curso
    path('cursos/', CursosView.as_view(), name='cursos-list'),
    path('curso/<int:pk>/', CursoView.as_view(), name='curso-detail'),
]
