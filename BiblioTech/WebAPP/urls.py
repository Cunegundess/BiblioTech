from django.urls import path
from . import views

urlpatterns = [
    path('', views.bibliotechPage, name='bibliotechPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('cadastro/', views.cadastroPage, name='cadastroPage'),
    path('senha/', views.senhaPage, name='senhaPage'),
    path('home/', views.homePage, name='homePage'),
    path('home/alunos/', views.alunosPage, name='alunosPage'),
    path('home/livros/', views.livrosPage, name='livrosPage'),
    path('home/livros/<int:pk>/', views.editarLivro, name='editarLivro'),
    path('home/livros/emprestimos', views.emprestimosPage, name='emprestimosPage'),
    path('home/autores/', views.autoresPage, name='autoresPage'),
    path('home/autores/<int:pk>/', views.editarAutor, name='editarAutor'),
    path('home/editoras/', views.editorasPage, name='editorasPage'),
    path('home/editoras/<int:pk>/', views.editarEditora, name='editarEditora')
]