from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class PublicadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicadora
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class GeneroLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLivro
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
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