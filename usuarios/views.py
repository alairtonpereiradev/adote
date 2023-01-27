from django.shortcuts import render
from django.http import HttpResponse
def cadastro(request):
    # return HttpResponse('Olá estou no cadastro')
    # A função render() recebe a requisição do usuário
    return render(request, 'cadastro.html')

