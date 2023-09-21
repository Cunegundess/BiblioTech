from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
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

# class UsuarioView():

#     @api_view(['GET'])
#     def get(request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)
    
#     @api_view(['POST'])
#     def post(request):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuariosView(APIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            usuario = self.queryset.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            usuario = self.queryset.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AutorListView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# class AutorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer

# # Publicadora
# class PublicadoraListView(generics.ListCreateAPIView):
#     queryset = Publicadora.objects.all()
#     serializer_class = PublicadoraSerializer

# class PublicadoraDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Publicadora.objects.all()
#     serializer_class = PublicadoraSerializer

# # Livro
# class LivroListView(generics.ListCreateAPIView):
#     queryset = Livro.objects.all()
#     serializer_class = LivroSerializer

# class LivroDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Livro.objects.all()
#     serializer_class = LivroSerializer

# # GeneroLivro
# class GeneroLivroListView(generics.ListCreateAPIView):
#     queryset = GeneroLivro.objects.all()
#     serializer_class = GeneroLivroSerializer

# class GeneroLivroDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = GeneroLivro.objects.all()
#     serializer_class = GeneroLivroSerializer

# # Usuario
# class UsuarioListView(generics.ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # Emprestimo
# class EmprestimoListView(generics.ListCreateAPIView):
#     queryset = Emprestimo.objects.all()
#     serializer_class = EmprestimoSerializer

# class EmprestimoDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Emprestimo.objects.all()
#     serializer_class = EmprestimoSerializer

# # Devolucao
# class DevolucaoListView(generics.ListCreateAPIView):
#     queryset = Devolucao.objects.all()
#     serializer_class = DevolucaoSerializer

# class DevolucaoDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Devolucao.objects.all()
#     serializer_class = DevolucaoSerializer

# # DetalhesLivro
# class DetalhesLivroListView(generics.ListCreateAPIView):
#     queryset = DetalhesLivro.objects.all()
#     serializer_class = DetalhesLivroSerializer

# class DetalhesLivroDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DetalhesLivro.objects.all()
#     serializer_class = DetalhesLivroSerializer
