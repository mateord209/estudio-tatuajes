from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pago
from .forms import PagoForm


class PagoListView(ListView):
    model = Pago
    template_name = 'pagos/pago_list.html'
    context_object_name = 'pagos'
    paginate_by = 10


class PagoDetailView(DetailView):
    model = Pago
    template_name = 'pagos/pago_detail.html'
    context_object_name = 'pago'


class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pagos/pago_form.html'
    success_url = reverse_lazy('pagos:pago_list')


class PagoUpdateView(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pagos/pago_form.html'
    success_url = reverse_lazy('pagos:pago_list')


class PagoDeleteView(DeleteView):
    model = Pago
    template_name = 'pagos/pago_confirm_delete.html'
    success_url = reverse_lazy('pagos:pago_list')