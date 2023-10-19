from django.apps import apps
from django.shortcuts import render
from API.models import *
# from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from WebAPP.forms import *
from .utils import *
from .filter import *

# Create your views here.
def bibliotechPage(request):
    return render(request, 'Pages/bibliotech.html')

def loginPage(request):
    context = {'form': adminLogin}
    return render(request, 'Pages/login.html', context)


def senhaPage(request):
    return render(request, 'Pages/senha.html')


def alunosPage(request):
    alunos = Aluno.objects.all()
    emprestimos = Emprestimo.objects.all()
    
    # Filtro
    filtro = AlunoFiltro(request.GET, queryset=alunos)
    alunos = filtro.qs

    # Paginação
    paginator = Paginator(alunos, 6)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)

    context = {'alunos': alunos, 'emprestimos': emprestimos, 'form': AlunoForm, 'filtro': filtro}
    return render(request, 'Pages/alunos.html', context)

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

    # Filtro
    filtro = LivroFiltro(request.GET, queryset=livros)
    livros = filtro.qs

    # Paginação
    paginator = Paginator(livros, 6)
    page = request.GET.get('page')
    livros = paginator.get_page(page)

    context = {'livros': livros, 'emprestimos': emprestimos, 'page_title': 'Livros', 'form': LivroForm, 'filtro': filtro}
    return render(request, 'Pages/livros.html', context)

def emprestimosPage(request):
    emprestimos = Emprestimo.objects.all()

    # Filtro
    filtro = EmprestimoFiltro(request.GET, queryset=emprestimos)
    emprestimos = filtro.qs

    # Paginação
    paginator = Paginator(emprestimos, 6)
    page = request.GET.get('page')
    emprestimos = paginator.get_page(page)

    context = {'emprestimos': emprestimos, 'page_title': 'Emprestimos', 'form': EmprestimoForm, 'filtro': filtro}
    return render(request, 'Pages/emprestimos.html', context)

def autoresPage(request):
    autores = Autor.objects.all()
    
    # Filtro
    filtro = AutoresFiltro(request.GET, queryset=autores)
    autores = filtro.qs

    # Paginação
    paginator = Paginator(autores, 6)
    page = request.GET.get('page')
    autores = paginator.get_page(page)
    
    context = {'autores': autores, 'page_title': 'Autores', 'form': AutorForm, 'filtro': filtro}
    return render(request, 'Pages/autores.html', context)

def editorasPage(request):
    editoras = Editora.objects.all()

    # Filtro
    filtro = EditoraFiltro(request.GET, queryset=editoras)
    editoras = filtro.qs

    # Paginação
    paginator = Paginator(editoras, 6)
    page = request.GET.get('page')
    editoras = paginator.get_page(page)
    
    context = {'editoras': editoras, 'page_title': 'Editoras', 'form': EditoraForm, 'filtro': filtro}
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

def cadastrarCurso(request):
    cursos = Curso.objects.all()
    
    # Filtro
    filtro = CursoFiltro(request.GET, queryset=cursos)
    cursos = filtro.qs

    context = {'cursos': cursos, 'page_title': 'Cursos', 'form': CursoForm, 'filtro': filtro}
    return render(request, 'Pages/cursos.html', context)


def pesquisa(request):
    resultados = []

    if request.method == 'POST':
        form = PesquisaForm(request.POST)

        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = pesquisar(consulta)
    else:
        form = PesquisaForm()

    context = {
        'form': form,
        'resultados': resultados,
    }

    return render(request, 'pesquisa.html', context)
