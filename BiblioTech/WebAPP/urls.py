from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.bibliotechPage, name='bibliotechPage'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

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
    path('home/cadastrar_curso', views.cadastrarCurso, name='cadastrarCurso')
]