from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.bibliotechPage, name='bibliotechPage'),

    path('home/', views.homePage, name='homePage'),
    path('home/pesquisa/', views.pesquisa, name='pesquisa'),
    path('home/alunos/', views.alunosPage, name='alunosPage'),
    path('home/livros/', views.livrosPage, name='livrosPage'),
    path('home/livros/<int:pk>/', views.editarLivro, name='editarLivro'),
    path('home/livros/emprestimos', views.emprestimosPage, name='emprestimosPage'),
    path('home/autores/', views.autoresPage, name='autoresPage'),
    path('home/autores/<int:pk>/', views.editarAutor, name='editarAutor'),
    path('home/editoras/', views.editorasPage, name='editorasPage'),
    path('home/editoras/<int:pk>/', views.editarEditora, name='editarEditora'),
    path('home/cadastrar_curso', views.cadastrarCurso, name='cadastrarCurso'),
    path('home/resultados_pesquisa/', views.resultados_pesquisa, name='resultados_pesquisa'),

]