from django.shortcuts import render
from API.models import Livro, Autor, Editora, Emprestimo, Usuario

# Create your views here.
def bibliotechPage(request):
    return render(request, 'Pages/initial.html')

def loginPage(request):
    return render(request, 'Pages/login.html')

def cadastroPage(request):
    return render(request, 'Pages/cadastro.html')

def senhaPage(request):
    return render(request, 'Pages/senha.html')

def minhaContaPage(request):
    return render(request, 'Pages/minhaConta.html')

def alunosPage(request):
    alunos = Usuario.objects.all()
    context = {'alunos': alunos}
    return render(request, 'Pages/alunosPage.html', context)

def homePage(request):
    livros = Livro.objects.all()
    editoras = Editora.objects.all()
    autores = Autor.objects.all()
    emprestimos = Emprestimo.objects.all()
    usuarios = Usuario.objects.all()
    context = {
        'livros': livros,
        'editoras': editoras,
        'autores': autores,
        'emprestimos': emprestimos,
        'usuarios': usuarios
    }
    return render(request, 'Pages/home.html', context)

def livrosPage(request):
    livros = Livro.objects.all()
    context = {'livros': livros, 'page_title': 'Livros'}
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
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
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