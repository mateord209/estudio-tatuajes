from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citas/', include('citas.urls')),
    path('clientes/', include('clientes.urls')),
    path('disenos/', include('disenos.urls')),
    path('pagos/', include('pagos.urls')),
    path('tatuadores/', include('tatuadores.urls')),
]