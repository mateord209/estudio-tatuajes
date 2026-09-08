from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tatuadores, name='lista_tatuadores'),
    path('nuevo/', views.crear_tatuador, name='crear_tatuador'),
    path('<int:pk>/editar/', views.editar_tatuador, name='editar_tatuador'),
    path('<int:pk>/eliminar/', views.eliminar_tatuador, name='eliminar_tatuador'),
]