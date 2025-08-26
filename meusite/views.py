from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordChangeView

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
            return render(request, 'login.html', {'error': 'Preencha todos os campos.'})
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        errors = []
        if not username or not email or not password:
            errors.append('Preencha todos os campos.')
        if User.objects.filter(username=username).exists():
            errors.append('Usuário já existe.')
        if User.objects.filter(email=email).exists():
            errors.append('Email já cadastrado.')
        if errors:
            return render(request, 'register.html', {'error': ' '.join(errors)})
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')
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
