from django.shortcuts import render, redirect, get_object_or_404
from .models import Diseno
from .forms import DisenoForm


def lista_disenos(request):
    disenos = Diseno.objects.all().order_by('nombre')
    return render(request, 'disenos/lista_disenos.html', {'disenos': disenos})


def crear_diseno(request):
    if request.method == 'POST':
        form = DisenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_disenos')
    else:
        form = DisenoForm()
    return render(request, 'disenos/form_diseno.html', {'form': form, 'titulo': 'Nuevo diseño'})


def editar_diseno(request, pk):
    diseno = get_object_or_404(Diseno, pk=pk)
    if request.method == 'POST':
        form = DisenoForm(request.POST, instance=diseno)
        if form.is_valid():
            form.save()
            return redirect('lista_disenos')
    else:
        form = DisenoForm(instance=diseno)
    return render(request, 'disenos/form_diseno.html', {'form': form, 'titulo': 'Editar diseño'})


def eliminar_diseno(request, pk):
    diseno = get_object_or_404(Diseno, pk=pk)
    if request.method == 'POST':
        diseno.delete()
        return redirect('lista_disenos')
    return render(request, 'disenos/confirmar_eliminar.html', {'diseno': diseno})