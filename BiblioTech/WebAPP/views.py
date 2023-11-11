import json
from django.apps import apps
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from API.models import *
# from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from WebAPP.forms import *
from .utils import *
from .filter import *
from django.contrib.auth.decorators import login_required
from Accounts.forms import *


# Create your views here.
def bibliotechPage(request):
    return render(request, 'Pages/bibliotech.html')


@login_required
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


@login_required
def editarAluno(request, pk):
    print(f"Received {request.method} request for aluno {pk}")
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Aluno atualizado com sucesso', 'redirect': '/home/alunos/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar aluno'}, status=400)
        
    elif request.method == 'DELETE':
        aluno.delete()
        return JsonResponse({'mensagem': 'Aluno excluído com sucesso', 'redirect': '/home/alunos/'})
    
    elif request.method == 'PUT':
        # Lê os dados brutos da solicitação
        data = json.loads(request.body.decode('utf-8'))
        form = AlunoForm(data, instance=aluno)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Aluno atualizado com sucesso', 'redirect': '/home/alunos/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar aluno'}, status=400)
        
    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'Pages/editPages/editarAluno.html', {'form': form, 'aluno': aluno})


@login_required
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


@login_required
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


@login_required
def editarLivro(request, pk):
    print(f"Received {request.method} request for Livro {pk}")
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Livro atualizado com sucesso', 'redirect': '/home/livros/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Livro'}, status=400)
        
    elif request.method == 'DELETE':
        livro.delete()
        return JsonResponse({'mensagem': 'Livro excluído com sucesso', 'redirect': '/home/livros/'})
    
    elif request.method == 'PUT':
        # Lê os dados brutos da solicitação
        data = json.loads(request.body.decode('utf-8'))
        form = LivroForm(data, instance=livro)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Livro atualizado com sucesso', 'redirect': '/home/livros/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Livro'}, status=400)
        
    else:
        form = LivroForm(instance=livro)

    return render(request, 'Pages/editPages/editarLivro.html', {'form': form, 'livro': livro})


@login_required
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


@login_required
def editarEmprestimo(request, pk):
    print(f"Received {request.method} request for Emprestimo {pk}")
    emprestimo = get_object_or_404(Emprestimo, pk=pk)

    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Emprestimo atualizado com sucesso', 'redirect': '/home/emprestimos/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Emprestimo'}, status=400)
        
    elif request.method == 'DELETE':
        emprestimo.delete()
        return JsonResponse({'mensagem': 'Emprestimo excluído com sucesso', 'redirect': '/home/emprestimos/'})
    
    elif request.method == 'PUT':
        # Lê os dados brutos da solicitação
        data = json.loads(request.body.decode('utf-8'))
        form = EmprestimoForm(data, instance=emprestimo)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Emprestimo atualizado com sucesso', 'redirect': '/home/emprestimos/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Emprestimo'}, status=400)
        
    else:
        form = EmprestimoForm(instance=emprestimo)

    return render(request, 'Pages/editPages/editarEmprestimo.html', {'form': form, 'emprestimo': emprestimo})


@login_required
def autoresPage(request):
    autores = Autor.objects.all()
    
    # Filtro
    filtro = AutoresFiltro(request.GET, queryset=autores)
    autores = filtro.qs

    # Paginação
    paginator = Paginator(autores, 6)
    page = request.GET.get('page')
    autores = paginator.get_page(page)

    # try:
    #     autores = paginator.page(page)
    # except PageNotAnInteger:
    #     autores = paginator.page(1)
    # except EmptyPage:
    #     autores = paginator.page(paginator.num_pages)
    
    context = {'autores': autores, 'page_title': 'Autores', 'form': AutorForm, 'filtro': filtro}
    return render(request, 'Pages/autores.html', context)


@login_required
def editarAutor(request, pk):
    print(f"Received {request.method} request for Autor {pk}")
    autor = get_object_or_404(Autor, pk=pk)

    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Autor atualizado com sucesso', 'redirect': '/home/autores/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Autor'}, status=400)
        
    elif request.method == 'DELETE':
        autor.delete()
        return JsonResponse({'mensagem': 'Autor excluído com sucesso', 'redirect': '/home/autores/'})
    
    elif request.method == 'PUT':
        # Lê os dados brutos da solicitação
        data = json.loads(request.body.decode('utf-8'))
        form = AutorForm(data, instance=autor)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Autor atualizado com sucesso', 'redirect': '/home/autores/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Autor'}, status=400)
        
    else:
        form = AutorForm(instance=autor)

    return render(request, 'Pages/editPages/editarAutor.html', {'form': form, 'autor': autor})


@login_required
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


@login_required
def editarEditora(request, pk):
    print(f"Received {request.method} request for Editora {pk}")
    editora = get_object_or_404(Editora, pk=pk)

    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Editora atualizado com sucesso', 'redirect': '/home/editoras/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Editora'}, status=400)
        
    elif request.method == 'DELETE':
        editora.delete()
        return JsonResponse({'mensagem': 'Editora excluído com sucesso', 'redirect': '/home/editoras/'})
    
    elif request.method == 'PUT':
        # Lê os dados brutos da solicitação
        data = json.loads(request.body.decode('utf-8'))
        form = EditoraForm(data, instance=editora)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Editora atualizado com sucesso', 'redirect': '/home/editoras/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Editora'}, status=400)
        
    else:
        form = EditoraForm(instance=editora)

    return render(request, 'Pages/editPages/editarEditora.html', {'form': form, 'editora': editora})


@login_required
def modalUser(request):
    Alunos = Aluno.objects.all()
    context = {'Alunos': Alunos}
    return render(request, context)


@login_required
def cursosPage(request):
    cursos = Curso.objects.all()
    
    # Filtro
    filtro = CursoFiltro(request.GET, queryset=cursos)
    cursos = filtro.qs

    context = {'cursos': cursos, 'page_title': 'Cursos', 'form': CursoForm, 'filtro': filtro}
    return render(request, 'Pages/cursos.html', context)


def editarCurso(request, pk):
    print(f"Received {request.method} request for Curso {pk}")
    curso = get_object_or_404(Curso, pk=pk)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Curso atualizado com sucesso', 'redirect': '/home/cursos/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Curso'}, status=400)
        
    elif request.method == 'DELETE':
        curso.delete()
        return JsonResponse({'mensagem': 'Curso excluído com sucesso', 'redirect': '/home/cursos/'})
    
    elif request.method == 'PUT':
        # Lê os dados brutos da solicitação
        data = json.loads(request.body.decode('utf-8'))
        form = CursoForm(data, instance=curso)
        if form.is_valid():
            form.save()
            return JsonResponse({'mensagem': 'Curso atualizado com sucesso', 'redirect': '/home/cursos/'})
        else:
            return JsonResponse({'erro': 'Erro ao atualizar Curso'}, status=400)
        
    else:
        form = CursoForm(instance=curso)

    return render(request, 'Pages/editPages/editarCurso.html', {'form': form, 'curso': curso})


# @login_required
# def pesquisa(request):
#     resultados = []

#     if request.method == 'POST':
#         form = PesquisaForm(request.POST)

#         if form.is_valid():
#             consulta = form.cleaned_data['consulta']
#             resultados = pesquisar(consulta)
#     else:
#         form = PesquisaForm()

#     context = {
#         'form': form,
#         'resultados': resultados,
#     }

#     return render(request, 'pesquisa.html', context)

def pesquisa(request):
    if 'consulta' in request.POST:
        consulta = request.POST['consulta']
        autores = Autor.objects.filter(nome__icontains=consulta)
        livros = Livro.objects.filter(titulo__icontains=consulta)
        # Adicione mais filtros para outros modelos, se necessário
    else:
        autores = Autor.objects.none()
        livros = Livro.objects.none()

    context = {
        'autores': autores,
        'livros': livros,
        'consulta': consulta
    }

    return render(request, 'resultadosPesquisa.html', context)

def resultados_pesquisa(request):
    consulta = request.GET.get('consulta')

    resultados_livros = Livro.objects.filter(titulo__icontains=consulta)
    resultados_autores = Autor.objects.filter(nome__icontains=consulta)
    resultados_editoras = Editora.objects.filter(nome__icontains=consulta)
    resultados_generoLivros = GeneroLivro.objects.filter(titulo__icontains=consulta)
    resultados_cursos = Curso.objects.filter(nome__icontains=consulta)
    resultados_alunos = Aluno.objects.filter(nome__icontains=consulta)
    resultados_emprestimos = Emprestimo.objects.filter(livro__icontains=consulta)
    resultados_devolucao = Devolucao.objects.filter(emprestimo__icontains=consulta)
    resultados_detalhesLivro = DetalhesLivro.objects.filter(autor__icontains=consulta)

    # Combine os resultados conforme necessário
    context = {
        'livros': list(resultados_livros.values()),  # Converte para uma lista de dicionários
        'autores': list(resultados_autores.values()),
        'editoras': list(resultados_editoras.values()),
        'generoLivros': list(resultados_generoLivros.values()),  # Converte para uma lista de dicionários
        'cursos': list(resultados_cursos.values()),
        'alunos': list(resultados_alunos.values()),
        'emprestimos': list(resultados_emprestimos.values()),  # Converte para uma lista de dicionários
        'devolucao': list(resultados_devolucao.values()),
        'detalhesLivro': list(resultados_detalhesLivro.values())
    }

    return render(request, 'resultadosPesquisa.html', context)
