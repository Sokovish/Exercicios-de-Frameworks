def erro_404(request, exception=None):
    return render(request, '404.html', status=404)

def erro_403(request, exception=None):
    return render(request, '403.html', status=403)

def erro_500(request):
    return render(request, '500.html', status=500)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy
from .models import Pessoa

def Home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        if not username or not password:
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já está em uso. Escolha outro.')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado. Use outro ou recupere a senha.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
        return redirect('login')
    return render(request, 'register.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    def form_valid(self, form):
        messages.info(self.request, 'Se o email estiver cadastrado, você receberá instruções para redefinir a senha.')
        return super().form_valid(form)

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Senha alterada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'lista_pessoas.html', {'pessoas': pessoas})
