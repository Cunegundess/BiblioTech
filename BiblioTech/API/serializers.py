from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class GeneroLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLivro
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'

class DevolucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucao
        fields = '__all__'

class DetalhesLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalhesLivro
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

