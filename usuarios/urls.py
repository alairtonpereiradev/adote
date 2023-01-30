from django.urls import path
from . import views

''' 
cadastro/ -> É o caminho na url
views.cadastro -> É a função que está config no arquivo views.py no diretorio usuarios
name -> é apenas o nome da urls   
'''
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
    path('sair/', views.sair, name="sair"),


]