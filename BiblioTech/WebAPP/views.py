from django.shortcuts import render


# Create your views here.
def bibliotechPage(request):
    return render(request, 'Pages/initial.html')

def loginPage(request):
    return render(request, 'Pages/login.html')

def cadastroPage(request):
    return render(request, 'Pages/cadastro.html')

def senhaPage(request):
    return render(request, 'Pages/senha.html')

def homePage(request):
    return render(request, 'Pages/home.html')

def livrosPage(request):
    return render(request, 'Pages/livros.html')

def autoresPage(request):
    return render(request, 'Pages/autores.html')

def editorasPage(request):
    return render(request, 'Pages/editoras.html')