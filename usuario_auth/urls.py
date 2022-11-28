from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_user, name='cadastro'),
    path('', views.login, name='login'),
]