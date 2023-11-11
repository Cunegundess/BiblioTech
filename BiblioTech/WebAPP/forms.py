from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from API.models import Autor, Editora, Livro, GeneroLivro, Curso, Aluno, Emprestimo, Devolucao, DetalhesLivro

class AutorForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = reverse_lazy('API:autores')
    #     self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade', 'data_nascimento']

class EditoraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('API:editoras')
        self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = Editora
        fields = ['nome', 'endereco', 'telefone']

class LivroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('API:livros')
        self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'descricao', 'ano_publicacao']

class GeneroLivroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('API:generolivros')
        self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = GeneroLivro
        fields = ['nome']

class CursoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('API:cursos')
        self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = Curso
        fields = ['nome', 'setor', 'semestres']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'senha', 'contato', 'ra', 'curso']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'nome',
            'email',
            'senha',
            'contato',
            'ra',
            'curso'
        )

class EmprestimoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('API:emprestimos')
        self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = Emprestimo
        fields = ['nome', 'livro', 'aluno', 'data_emprestimo', 'data_devolucao']

class DevolucaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('API:devolucoes')
        self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = Devolucao
        fields = ['emprestimo', 'multa']

class DetalhesLivroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('API:detalheslivros')
        self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))

    class Meta:
        model = DetalhesLivro
        fields = ['autor', 'editora', 'genero', 'unidades', 'emprestimo']

class PesquisaForm(forms.Form):
    consulta = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Livros, Autores...'}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = reverse_lazy('API:detalheslivros')
    #     self.helper.form_method = 'POST'
        # self.helper.add_input(Submit('submit', 'Salvar'))


