from django.shortcuts import render
from django.http import HttpResponse
# importa o modelo usuários do banco de dodos modelo do django feito no migrate
from django.contrib.auth.models import User
# importação das mensagem de alerta
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def cadastro(request):
    # Este if não permite o usuário já logado ter acesso a pagina de login e cadastro de usuários.
    if request.user.is_authenticated:
        return redirect(request, '/divulgar/novo_pet')
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
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 \
                or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return render(request, 'cadastro.html')
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Por favor digite a senha e confirma senha iguais.')
            return render(request, 'cadastro.html')

# https://docs.djangoproject.com/en/4.1/topics/auth/default/
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

def logar(request):
    # Este if não permite o usuário já logado ter acesso a pagina de login e cadastro de usuários.
    if request.user.is_authenticated:
        return redirect(request, '/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(
            username=nome,
            password=senha)
    if user is not None:
        login(request, user)
        return redirect('/divulgar/novo_pet')
    else:
        messages.add_message(request, constants.ERROR, 'Usuário ou Senha inválidos.')
        return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('/auth/login')

