from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import *
from .serializers import *
from datetime import datetime
from .utils import converter_dataNascimento, converter_dataEmprestimo, converter_dataDevolucao
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


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
    'alunos/',
    'aluno/<int:pk>/',
    'emprestimos/',
    'emprestimo/<int:pk>/',
    'devolucoes/',
    'devolucao/<int:pk>/',
    'detalheslivros/',
    'detalheslivro/<int:pk>/',
    'cursos/',
    'curso/<int:pk>/',
    ]

    return render(request, 'routes.html', {'routes': routes})


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


@api_view(['GET'])
def usuarios(request):
    usuarios = User.objects.all()
    serializer = UserSerializer(usuarios, many=True)  # Crie um serializer para os usuários
    return Response(serializer.data)


class AlunosView(APIView):
    queryset = Aluno.objects.all().order_by("nome")
    serializer_class = AlunoSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        alunos = self.queryset
        paginator = self.pagination_class()  # Instancia a classe de paginação
        page = paginator.paginate_queryset(alunos, request)  # Pagina os resultados

        if page is not None:
            serializer = AlunoSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            aluno = self.queryset.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class AlunoView(APIView):
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Aluno.objects.all()
    
    def get_object(self, pk):
        try:
            return Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return None
        

    def get(self, request, pk):
        aluno = self.get_object(pk)
        if aluno is not None:
            serializer = self.serializer_class(aluno)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        aluno = self.get_object(pk)
        if aluno is not None:
            serializer = self.serializer_class(aluno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        aluno = self.get_object(pk)
        if aluno is not None:
            aluno.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AutoresView(APIView):
    queryset = Autor.objects.all().order_by("nome")
    serializer_class = AutorSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        autores = self.queryset
        paginator = self.pagination_class()  # Instancia a classe de paginação
        page = paginator.paginate_queryset(autores, request)  # Pagina os resultados

        if page is not None:
            serializer = AutorSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Faça uma cópia editável do QueryDict
        dados_editaveis = request.data.copy()

        data_nascimento_str = dados_editaveis.get('data_nascimento')
        data_nascimento = converter_dataNascimento(data_nascimento_str)

        if data_nascimento is not None:
            dados_editaveis['data_nascimento'] = data_nascimento

            serializer = self.serializer_class(data=dados_editaveis)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Formato de data inválido'}, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk):
        try:
            autor = self.queryset.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AutorView(APIView):
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Autor.objects.all()

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
    queryset = Editora.objects.all().order_by("nome")
    serializer_class = EditoraSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        editoras = self.queryset
        paginator = self.pagination_class()  # Instancia a classe de paginação
        page = paginator.paginate_queryset(editoras, request)  # Pagina os resultados

        if page is not None:
            serializer = EditoraSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = EditoraSerializer(editoras, many=True)
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
    queryset = Editora.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Editora.objects.all()

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
    queryset = Livro.objects.all().order_by("titulo")
    serializer_class = LivroSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        livros = self.queryset
        paginator = self.pagination_class()  # Instancia a classe de paginação
        page = paginator.paginate_queryset(livros, request)  # Pagina os resultados

        if page is not None:
            serializer = LivroSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = LivroSerializer(livros, many=True)
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
    queryset = Livro.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Livro.objects.all()

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
    queryset = Emprestimo.objects.all().order_by("livro")
    serializer_class = EmprestimoSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        emprestimos = self.queryset
        paginator = self.pagination_class()  # Instancia a classe de paginação
        page = paginator.paginate_queryset(emprestimos, request)  # Pagina os resultados

        if page is not None:
            serializer = EmprestimoSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = EmprestimoSerializer(emprestimos, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        dados_editaveis = request.data.copy()

        data_emprestimo_str = dados_editaveis.get('data_emprestimo')
        data_emprestimo = converter_dataEmprestimo(data_emprestimo_str)
        data_devolucao_str = dados_editaveis.get('data_devolucao')
        data_devolucao = converter_dataDevolucao(data_devolucao_str)

        if data_emprestimo and data_devolucao is not None:
            dados_editaveis['data_emprestimo'] = data_emprestimo
            dados_editaveis['data_devolucao'] = data_devolucao

            serializer = self.serializer_class(data=dados_editaveis)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Formato de data inválido'}, status=status.HTTP_400_BAD_REQUEST)


        # serializer = self.serializer_class(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    serializer_class = EmprestimoSerializer
    queryset = Emprestimo.objects.all()  # Adicione esta linha

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Emprestimo.objects.all()

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
    queryset = Devolucao.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Devolucao.objects.all()

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
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(detalhes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class DetalhesLivroView(APIView):
    serializer_class = DetalhesLivroSerializer
    queryset = DetalhesLivro.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return DetalhesLivro.objects.all()

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
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneroLivroView(APIView):
    serializer_class = DetalhesLivroSerializer
    queryset = GeneroLivro.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return GeneroLivro.objects.all()

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
    

class CursosView(APIView):
    queryset = Curso.objects.all().order_by("nome")
    serializer_class = CursoSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        cursos = self.queryset
        paginator = self.pagination_class()  # Instancia a classe de paginação
        page = paginator.paginate_queryset(cursos, request)  # Pagina os resultados

        if page is not None:
            serializer = CursoSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            curso = self.queryset.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CursoView(APIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()  # Adicione esta linha

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Curso.objects.all()

    def get_object(self, pk):
        try:
            return CursoSerializer.objects.get(pk=pk)
        except CursoSerializer.DoesNotExist:
            return None

    def get(self, request, pk):
        curso = self.get_object(pk)
        if curso is not None:
            serializer = self.serializer_class(curso)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        curso = self.get_object(pk)
        if curso is not None:
            serializer = self.serializer_class(curso, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        curso = self.get_object(pk)
        if curso is not None:
            curso.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

def pesquisa(request):
    consulta = request.GET.get('consulta', '')

    # Realize a lógica de pesquisa aqui
    resultados_livros = Livro.objects.filter(titulo__icontains=consulta)
    resultados_autores = Autor.objects.filter(nome__icontains=consulta)
    resultados_editoras = Editora.objects.filter(nome__icontains=consulta)
    resultados_cursos = Curso.objects.filter(nome__icontains=consulta)
    resultados_alunos = Aluno.objects.filter(nome__icontains=consulta)
    resultados_emprestimos = Emprestimo.objects.filter(nome__icontains=consulta)

    # Serialize os resultados
    livros_serialized = LivroSerializer(resultados_livros, many=True).data
    autores_serialized = AutorSerializer(resultados_autores, many=True).data
    editoras_serialized = EditoraSerializer(resultados_editoras, many=True).data
    cursos_serialized = CursoSerializer(resultados_cursos, many=True).data
    alunos_serialized = AlunoSerializer(resultados_alunos, many=True).data
    emprestimos_serialized = EmprestimoSerializer(resultados_emprestimos, many=True).data

    # Combine os resultados
    resultados = {
        'livros': livros_serialized,
        'autores': autores_serialized,
        'editoras': editoras_serialized,
        'cursos': cursos_serialized,
        'alunos': alunos_serialized,
        'emprestimos': emprestimos_serialized,
    }

    return JsonResponse(resultados)