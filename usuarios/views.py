from django.shortcuts import render
from django.http import HttpResponse
def cadastro(request):
    # return HttpResponse('Olá estou no cadastro')
    # A função render() recebe a requisição do usuário
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        # print(nome, email, senha, confirmar_senha)
        # Validação dos campos do formulario
        if  len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            return render(request, 'cadastro.html')
        if senha != confirmar_senha:
            return render(request, 'cadastro.html')

        return HttpResponse(f'{nome}, {email}, {senha}, {confirmar_senha}')

