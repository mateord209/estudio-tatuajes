from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('nueva/', views.crear_cita, name='crear_cita'),
    path('<int:pk>/editar/', views.editar_cita, name='editar_cita'),
    path('<int:pk>/eliminar/', views.eliminar_cita, name='eliminar_cita'),
]