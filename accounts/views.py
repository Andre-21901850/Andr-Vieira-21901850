from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from .forms import RegistoForm
from .models import MagicToken

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})

def login_view(request):
    erro = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio')
        else:
            erro = 'Credenciais inválidas.'
    return render(request, 'accounts/login.html', {'erro': erro})

def logout_view(request):
    logout(request)
    return redirect('login')

def magic_link_view(request):
    mensagem = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = MagicToken.objects.create(user=user)
            link = request.build_absolute_uri(
                reverse('magic_link_login', args=[str(token.token)])
            )
            send_mail(
                'O teu link de acesso',
                f'Clica aqui para entrar: {link}',
                'noreply@portfolio.com',
                [email],
            )
            mensagem = 'Link enviado! Verifica o terminal do servidor.'
        except User.DoesNotExist:
            mensagem = 'Email não encontrado.'
    return render(request, 'accounts/magic_link.html', {'mensagem': mensagem})

def magic_link_login_view(request, token):
    magic = get_object_or_404(MagicToken, token=token, usado=False)
    magic.usado = True
    magic.save()
    login(request, magic.user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('portfolio')