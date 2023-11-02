from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *

# Create your views here.
def loginPage(request):
    context = {'form': adminLogin}
    return render(request, 'registration/login.html', context)


class cadastroView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/cadastro.html"