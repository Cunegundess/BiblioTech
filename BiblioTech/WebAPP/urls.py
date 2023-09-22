from django.urls import path
from . import views

urlpatterns = [
    path('', views.bibliotechPage, name='bibliotechPage'),
    path('login/', views.loginPage, name='loginPage')
]