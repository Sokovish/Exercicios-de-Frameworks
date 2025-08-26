
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
]

