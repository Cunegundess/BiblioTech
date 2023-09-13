from django.urls import path
from .views import *

urlpatterns = [
    path('', routesList, name='routes-list'),
    # Autor
    path('autor/', AutorListView.as_view(), name='autor-list'),
    path('autor/<int:pk>/', AutorDetailView.as_view(), name='autor-detail'),

    # Publicadora
    path('publicadora/', PublicadoraListView.as_view(), name='publicadora-list'),
    path('publicadora/<int:pk>/', PublicadoraDetailView.as_view(), name='publicadora-detail'),

    # Livro
    path('livro/', LivroListView.as_view(), name='livro-list'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detail'),

    # GeneroLivro
    path('generolivro/', GeneroLivroListView.as_view(), name='generolivro-list'),
    path('generolivro/<int:pk>/', GeneroLivroDetailView.as_view(), name='generolivro-detail'),

    # Usuario
    path('usuario/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    # Emprestimo
    path('emprestimo/', EmprestimoListView.as_view(), name='emprestimo-list'),
    path('emprestimo/<int:pk>/', EmprestimoDetailView.as_view(), name='emprestimo-detail'),

    # Devolucao
    path('devolucao/', DevolucaoListView.as_view(), name='devolucao-list'),
    path('devolucao/<int:pk>/', DevolucaoDetailView.as_view(), name='devolucao-detail'),

    # DetalhesLivro
    path('detalheslivro/', DetalhesLivroListView.as_view(), name='detalheslivro-list'),
    path('detalheslivro/<int:pk>/', DetalhesLivroDetailView.as_view(), name='detalheslivro-detail'),
]
