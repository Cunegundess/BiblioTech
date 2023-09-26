from django.urls import path
from . import views

urlpatterns = [
    path('', views.bibliotechPage, name='bibliotechPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('cadastro/', views.cadastroPage, name='cadastroPage'),
    path('senha/', views.senhaPage, name='senhaPage'),
    path('home/', views.homePage, name='homePage'),
    path('livros/', views.livrosPage, name='livrosPage'),
    path('autores/', views.autoresPage, name='autoresPage'),
    path('editoras/', views.editorasPage, name='editorasPage'),
]