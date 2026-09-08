from django.urls import path
from . import views

app_name = 'pagos'

urlpatterns = [
    path('', views.PagoListView.as_view(), name='pago_list'),
    path('nuevo/', views.PagoCreateView.as_view(), name='pago_create'),
    path('<int:pk>/', views.PagoDetailView.as_view(), name='pago_detail'),
    path('<int:pk>/editar/', views.PagoUpdateView.as_view(), name='pago_update'),
    path('<int:pk>/eliminar/', views.PagoDeleteView.as_view(), name='pago_delete'),
]