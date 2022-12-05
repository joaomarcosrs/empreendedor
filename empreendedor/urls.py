from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario_auth.urls')),
    path('home/', include('emp_cadastro.urls')),
]
