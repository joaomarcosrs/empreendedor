from django.urls import path
from . import views

urlpatterns = [
    path('home/cadastro/', views.cadastro_user, name='cadastro'),
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home')
]