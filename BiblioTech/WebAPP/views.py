from django.shortcuts import render
from API.models import Livro, Autor, Editora, Emprestimo, Aluno
# from django.contrib.auth.forms import UserCreationForm
from WebAPP.forms import *

# Create your views here.
def bibliotechPage(request):
    return render(request, 'Pages/initial.html')

def loginPage(request):
    context = {'form': adminLogin}
    return render(request, 'Pages/login.html', context)

def cadastroPage(request):
    return render(request, 'Pages/cadastro.html')

def senhaPage(request):
    return render(request, 'Pages/senha.html')


def alunosPage(request):
    alunos = Aluno.objects.all()
    emprestimos = Emprestimo.objects.all()
    context = {'alunos': alunos, 'emprestimos': emprestimos, 'form': AlunoForm}
    return render(request, 'Pages/alunosPage.html', context)

def homePage(request):
    livros = Livro.objects.all()[:5]
    editoras = Editora.objects.all()[:5]
    autores = Autor.objects.all()[:5]
    emprestimos = Emprestimo.objects.all()[:5]
    alunos = Aluno.objects.all()[:5]
    context = {
        'livros': livros,
        'editoras': editoras,
        'autores': autores,
        'emprestimos': emprestimos,
        'alunos': alunos
    }
    return render(request, 'Pages/home.html', context)

def livrosPage(request):
    livros = Livro.objects.all()
    emprestimos = Emprestimo.objects.all()
    context = {'livros': livros, 'emprestimos': emprestimos, 'page_title': 'Livros'}
    return render(request, 'Pages/livros.html', context)

def emprestimosPage(request):
    emprestimos = Emprestimo.objects.all()
    context = {'emprestimos': emprestimos, 'page_title': 'Emprestimos'}
    return render(request, 'Pages/emprestimos.html', context)

def autoresPage(request):
    autores = Autor.objects.all()
    context = {'autores': autores, 'page_title': 'Autores'}
    return render(request, 'Pages/autores.html', context)

def editorasPage(request):
    editoras = Editora.objects.all()
    context = {'editoras': editoras, 'page_title': 'Editoras'}
    return render(request, 'Pages/editoras.html', context)

def modalUser(request):
    Alunos = Aluno.objects.all()
    context = {'Alunos': Alunos}
    return render(request, context)

def editarLivro(request, pk):
    # livros = Livro.objects.all()
    # context = {'livros': livros}
    titulo = {
        'page_title': 'Livros'
    }
    
    return render(request, 'Pages/editarLivro.html', titulo)

def editarAutor(request, pk):
    # autores = Autor.objects.all()
    # context = {'autores': autores}
    titulo = {
        'page_title': 'Autores'
    }
    return render(request, 'Pages/editarAutor.html', titulo)

def editarEditora(request, pk):
    # editoras = Editora.objects.all()
    # context = {'editoras': editoras}
    titulo = {
        'page_title': 'Editoras'
    }
    return render(request, 'Pages/editarEditora.html', titulo)