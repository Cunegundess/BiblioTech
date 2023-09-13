from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_falecimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Publicadora(models.Model):
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


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    is_funcionario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()

    def __str__(self):
        return f'{self.livro} emprestado por {self.usuario}'

class Devolucao(models.Model):
    emprestimo = models.OneToOneField(Emprestimo, on_delete=models.CASCADE)
    data_devolucao = models.DateField(auto_now_add=True)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Devolução de {self.emprestimo}'

class DetalhesLivro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    publicadora = models.ForeignKey(Publicadora, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(GeneroLivro, on_delete=models.SET_NULL, null=True)
    unidades = models.PositiveIntegerField()
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.autor} - {self.publicadora} - {self.genero}'