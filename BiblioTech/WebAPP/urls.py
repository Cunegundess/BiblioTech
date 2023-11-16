from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.bibliotechPage, name='bibliotechPage'),

    path('home/', views.homePage, name='homePage'),
    # path('home/pesquisa/', views.pesquisa, name='pesquisa'),
    path('home/alunos/', views.alunosPage, name='alunosPage'),
    path('home/alunos/<int:pk>', views.editarAluno, name='editarAluno'),
    path('home/livros/', views.livrosPage, name='livrosPage'),
    path('home/livros/<int:pk>/', views.editarLivro, name='editarLivro'),
    path('home/emprestimos', views.emprestimosPage, name='emprestimosPage'),
    path('home/emprestimos/<int:pk>/', views.editarEmprestimo, name='editarEmprestimo'),
    path('home/autores/', views.autoresPage, name='autoresPage'),
    path('home/autores/<int:pk>/', views.editarAutor, name='editarAutor'),
    path('home/editoras/', views.editorasPage, name='editorasPage'),
    path('home/editoras/<int:pk>/', views.editarEditora, name='editarEditora'),
    path('home/cursos', views.cursosPage, name='cursosPage'),
    path('home/curso/<int:pk>/', views.editarCurso, name='editarCurso'),
    path('home/resultados_pesquisa/', views.search_view, name='search_view'),

]