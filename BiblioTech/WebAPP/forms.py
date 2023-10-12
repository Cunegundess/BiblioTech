from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from API.models import Autor, Editora, Livro, GeneroLivro, Curso, Aluno, Emprestimo, Devolucao, DetalhesLivro

class adminLogin(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        super().__init__(*args, **kwargs)
        
    usuario = forms.CharField()
    senha = forms.CharField()

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade', 'data_nascimento']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'endereco', 'telefone']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'descricao', 'ano_publicacao']

class GeneroLivroForm(forms.ModelForm):
    class Meta:
        model = GeneroLivro
        fields = ['nome']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'setor', 'semestres']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'senha', 'contato', 'ra', 'curso']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'aluno', 'data_devolucao']

class DevolucaoForm(forms.ModelForm):
    class Meta:
        model = Devolucao
        fields = ['emprestimo', 'multa']

class DetalhesLivroForm(forms.ModelForm):
    class Meta:
        model = DetalhesLivro
        fields = ['autor', 'editora', 'genero', 'unidades', 'emprestimo']

