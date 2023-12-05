from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
    
class GeneroLivro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    semestres = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    ra = models.CharField(max_length=100, unique=True) 
    data_cadastro = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    nome = models.CharField(max_length=100, default="NomeEmprestimo", null=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

    def __str__(self):
        return f'{self.livro} emprestado por {self.aluno}'

class Devolucao(models.Model):
    emprestimo = models.OneToOneField(Emprestimo, on_delete=models.CASCADE)
    data_devolucao = models.DateField(auto_now_add=True)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Devolução de {self.emprestimo}'

class DetalhesLivro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(GeneroLivro, on_delete=models.SET_NULL, null=True)
    unidades = models.PositiveIntegerField()
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.autor} - {self.Editora} - {self.genero}'
    
class Filtro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(GeneroLivro, on_delete=models.SET_NULL, null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.SET_NULL, null=True)
    devolucao = models.ForeignKey(Devolucao, on_delete=models.SET_NULL, null=True)
    detalhesLivro = models.ForeignKey(DetalhesLivro, on_delete=models.SET_NULL, null=True)

class Pesquisa(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(GeneroLivro, on_delete=models.SET_NULL, null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.SET_NULL, null=True)
    devolucao = models.ForeignKey(Devolucao, on_delete=models.SET_NULL, null=True)
    detalhesLivro = models.ForeignKey(DetalhesLivro, on_delete=models.SET_NULL, null=True)