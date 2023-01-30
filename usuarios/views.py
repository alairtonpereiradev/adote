from django.shortcuts import render
from django.http import HttpResponse
# importa o modelo usuários do banco de dodos modelo do django feito no migrate
from django.contrib.auth.models import User
# importação das mensagem de alerta
from django.contrib import messages
from django.contrib.messages import constants

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
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return render(request, 'cadastro.html')
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Por favor digite a senha e confirma senha iguais.')
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return render(request, 'cadastro.html')
        except:
            messages.add_message(request, constants.ERROR, 'Desculpe, Erro interno do sistema. Tente mais tarde.')
            return render(request, 'cadastro.html')



        return HttpResponse(f'{nome}, {email}, {senha}, {confirmar_senha}')

