from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

def routesList(request):
    routes = [
    'autores/',
    'autor/<int:pk>/',
    'editoras/',
    'editora/<int:pk>/',
    'livros/',
    'livro/<int:pk>/',
    'generolivros/',
    'generolivro/<int:pk>/',
    'usuarios/',
    'usuario/<int:pk>/',
    'emprestimos/',
    'emprestimo/<int:pk>/',
    'devolucoes/',
    'devolucao/<int:pk>/',
    'detalheslivros/',
    'detalheslivro/<int:pk>/',
    ]

    return render(request, 'routes.html', {'routes': routes})
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
class UsuarioView(APIView):
    serializer_class = UsuarioSerializer

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return None

    def get(self, request, pk):
        usuario = self.get_object(pk)
        if usuario is not None:
            serializer = self.serializer_class(usuario)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        usuario = self.get_object(pk)
        if usuario is not None:
            serializer = self.serializer_class(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        usuario = self.get_object(pk)
        if usuario is not None:
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class AutoresView(APIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

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
            autor = self.queryset.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AutorView(APIView):

    serializer_class = AutorSerializer

    def get_object(self, pk):
        try:
            return Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            return None

    def get(self, request, pk):
        autor = self.get_object(pk)
        if autor is not None:
            serializer = self.serializer_class(autor)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        autor = self.get_object(pk)
        if autor is not None:
            serializer = self.serializer_class(autor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        autor = self.get_object(pk)
        if autor is not None:
            autor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class EditorasView(APIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

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
            editora = self.queryset.get(pk=pk)
        except Editora.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(editora, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
class EditoraView(APIView):
    serializer_class = EditoraSerializer

    def get_object(self, pk):
        try:
            return Editora.objects.get(pk=pk)
        except Editora.DoesNotExist:
            return None

    def get(self, request, pk):
        editora = self.get_object(pk)
        if editora is not None:
            serializer = self.serializer_class(editora)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        editora = self.get_object(pk)
        if editora is not None:
            serializer = self.serializer_class(editora, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        editora = self.get_object(pk)
        if editora is not None:
            editora.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class LivrosView(APIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

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
            livro = self.queryset.get(pk=pk)
        except Livro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LivroView(APIView):
    serializer_class = LivroSerializer

    def get_object(self, pk):
        try:
            return Livro.objects.get(pk=pk)
        except Livro.DoesNotExist:
            return None

    def get(self, request, pk):
        livro = self.get_object(pk)
        if livro is not None:
            serializer = self.serializer_class(livro)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        livro = self.get_object(pk)
        if livro is not None:
            serializer = self.serializer_class(livro, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        livro = self.get_object(pk)
        if livro is not None:
            livro.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class EmprestimosView(APIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

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
            emprestimo = self.queryset.get(pk=pk)
        except Emprestimo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(emprestimo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
class EmprestimoView(APIView):
    serializer_class = UsuarioSerializer

    def get_object(self, pk):
        try:
            return Emprestimo.objects.get(pk=pk)
        except Emprestimo.DoesNotExist:
            return None

    def get(self, request, pk):
        emprestimo = self.get_object(pk)
        if emprestimo is not None:
            serializer = self.serializer_class(emprestimo)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        emprestimo = self.get_object(pk)
        if emprestimo is not None:
            serializer = self.serializer_class(emprestimo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        emprestimo = self.get_object(pk)
        if emprestimo is not None:
            emprestimo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class DevolucoesView(APIView):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer

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
            devolucao = self.queryset.get(pk=pk)
        except Devolucao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(devolucao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DevolucaoView(APIView):

    serializer_class = DevolucaoSerializer

    def get_object(self, pk):
        try:
            return Devolucao.objects.get(pk=pk)
        except Devolucao.DoesNotExist:
            return None

    def get(self, request, pk):
        devolucao = self.get_object(pk)
        if devolucao is not None:
            serializer = self.serializer_class(devolucao)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        devolucao = self.get_object(pk)
        if devolucao is not None:
            serializer = self.serializer_class(devolucao, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        devolucao = self.get_object(pk)
        if devolucao is not None:
            devolucao.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class DetalhesLivrosView(APIView):
    queryset = DetalhesLivro.objects.all()
    serializer_class = DetalhesLivroSerializer

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
            detalhes = self.queryset.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(detalhes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
class DetalhesLivroView(APIView):
    serializer_class = DetalhesLivroSerializer

    def get_object(self, pk):
        try:
            return DetalhesLivro.objects.get(pk=pk)
        except DetalhesLivro.DoesNotExist:
            return None

    def get(self, request, pk):
        detalhes = self.get_object(pk)
        if detalhes is not None:
            serializer = self.serializer_class(detalhes)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        detalhes = self.get_object(pk)
        if detalhes is not None:
            serializer = self.serializer_class(detalhes, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        detalhes = self.get_object(pk)
        if detalhes is not None:
            detalhes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
class GeneroLivrosView(APIView):
    queryset = GeneroLivro.objects.all()
    serializer_class = GeneroLivroSerializer

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
            genero = self.queryset.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
class GeneroLivroView(APIView):
    serializer_class = DetalhesLivroSerializer

    def get_object(self, pk):
        try:
            return GeneroLivro.objects.get(pk=pk)
        except GeneroLivro.DoesNotExist:
            return None

    def get(self, request, pk):
        genero = self.get_object(pk)
        if genero is not None:
            serializer = self.serializer_class(genero)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        genero = self.get_object(pk)
        if genero is not None:
            serializer = self.serializer_class(genero, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        genero = self.get_object(pk)
        if genero is not None:
            genero.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)