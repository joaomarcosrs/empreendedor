from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('registro_atendimento/', views.registro_atendimento, name='registro_atendimento'),
    path('registros/', views.registros, name='registros'),
] + static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)