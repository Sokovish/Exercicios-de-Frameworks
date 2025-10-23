
from django.contrib import admin
from django.urls import path
from meusite import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('lista_pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('gerente_dashboard/', views.gerente_dashboard, name='gerente_dashboard'),

    path('erro_404/', views.erro_404, name='erro_404'),
    path('erro_403/', views.erro_403, name='erro_403'),
    path('erro_500/', views.erro_500, name='erro_500'),
]



