from django.db import router
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

app_name = 'API'


urlpatterns = [
    path('', routesList, name='routes-list'),

    path('pesquisa/', pesquisa, name='pesquisa'),

    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Autor
    path('autores/', AutoresView.as_view(), name='autores'),
    path('autor/<int:pk>/', AutorView.as_view(), name='autor'),

    # Editora
    path('editoras/', EditorasView.as_view(), name='editoras'),
    path('editora/<int:pk>/', EditoraView.as_view(), name='editora'),

    # Livro
    path('livros/', LivrosView.as_view(), name='livros'),
    path('livro/<int:pk>/', LivroView.as_view(), name='livro'),

    # GeneroLivro
    path('generolivros/', GeneroLivrosView.as_view(), name='generolivros'),
    path('generolivro/<int:pk>/', GeneroLivroView.as_view(), name='generolivro'),

    # Usuario
    path('alunos/', AlunosView.as_view(), name='alunos'),
    path('aluno/<int:pk>/', AlunoView.as_view(), name='aluno'),

    # Emprestimo
    path('emprestimos/', EmprestimosView.as_view(), name='emprestimos'),
    path('emprestimo/<int:pk>/', EmprestimoView.as_view(), name='emprestimo'),

    # Devolucao
    path('devolucoes/', DevolucoesView.as_view(), name='devolucoes'),
    path('devolucao/<int:pk>/', DevolucaoView.as_view(), name='devolucao'),

    # DetalhesLivro
    path('detalheslivros/', DetalhesLivrosView.as_view(), name='detalheslivros'),
    path('detalheslivro/<int:pk>/', DetalhesLivrosView.as_view(), name='detalheslivro'),

    # Curso
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('curso/<int:pk>/', CursoView.as_view(), name='curso'),
]

router = DefaultRouter()
router.register('user', UserViewset, basename='user')
urlpatterns += router.urls