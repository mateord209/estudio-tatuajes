from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_disenos, name='lista_disenos'),
    path('nuevo/', views.crear_diseno, name='crear_diseno'),
    path('<int:pk>/editar/', views.editar_diseno, name='editar_diseno'),
    path('<int:pk>/eliminar/', views.eliminar_diseno, name='eliminar_diseno'),
]