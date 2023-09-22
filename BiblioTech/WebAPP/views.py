from django.shortcuts import render


# Create your views here.
def bibliotechPage(request):
    return render(request, 'Pages/bibliotech.html')

def loginPage(request):
    return render(request, 'Pages/login.html')