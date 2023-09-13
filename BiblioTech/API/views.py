from django.shortcuts import render
from rest_framework import generics
from .models import Autor, Publicadora, Livro, GeneroLivro, Usuario, Emprestimo, Devolucao, DetalhesLivro
from .serializers import *

def routesList(request):
    routes = [
    'autor/',
    'autor/<int:pk>/',
    'publicadora/',
    'publicadora/<int:pk>/',
    'livro/',
    'livro/<int:pk>/',
    'generolivro/',
    'generolivro/<int:pk>/',
    'usuario/',
    'usuario/<int:pk>/',
    'emprestimo/',
    'emprestimo/<int:pk>/',
    'devolucao/',
    'devolucao/<int:pk>/',
    'detalheslivro/',
    'detalheslivro/<int:pk>/',
    ]

    return render(request, 'routes.html', {'routes': routes})

class AutorListView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# Publicadora
class PublicadoraListView(generics.ListCreateAPIView):
    queryset = Publicadora.objects.all()
    serializer_class = PublicadoraSerializer

class PublicadoraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicadora.objects.all()
    serializer_class = PublicadoraSerializer

# Livro
class LivroListView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# GeneroLivro
class GeneroLivroListView(generics.ListCreateAPIView):
    queryset = GeneroLivro.objects.all()
    serializer_class = GeneroLivroSerializer

class GeneroLivroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneroLivro.objects.all()
    serializer_class = GeneroLivroSerializer

# Usuario
class UsuarioListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Emprestimo
class EmprestimoListView(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

# Devolucao
class DevolucaoListView(generics.ListCreateAPIView):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer

class DevolucaoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer

# DetalhesLivro
class DetalhesLivroListView(generics.ListCreateAPIView):
    queryset = DetalhesLivro.objects.all()
    serializer_class = DetalhesLivroSerializer

class DetalhesLivroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalhesLivro.objects.all()
    serializer_class = DetalhesLivroSerializer
