from django.shortcuts import render
# from BiblioTech.API.models import Livro, Autor, Editora

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

def homePage(request):
    return render(request, 'Pages/home.html')

def livrosPage(request):
    # livros = Livro.objects.all()
    # context = {'livros': livros}
    titulo = {
        'page_title': 'Livros'
    }
    
    return render(request, 'Pages/livros.html', titulo)

def emprestimosPage(request):
    # editoras = Editora.objects.all()
    # context = {'editoras': editoras}
    titulo = {
        'page_title': 'Empréstimos'
    }
    return render(request, 'Pages/emprestimos.html', titulo)

def autoresPage(request):
    # autores = Autor.objects.all()
    # context = {'autores': autores}
    titulo = {
        'page_title': 'Autores'
    }
    return render(request, 'Pages/autores.html', titulo)

def editorasPage(request):
    # editoras = Editora.objects.all()
    # context = {'editoras': editoras}
    titulo = {
        'page_title': 'Editoras'
    }
    return render(request, 'Pages/editoras.html', titulo)

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