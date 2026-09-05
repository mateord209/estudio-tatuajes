from django.shortcuts import render, redirect, get_object_or_404
from .models import Tatuador
from .forms import TatuadorForm


def lista_tatuadores(request):
    tatuadores = Tatuador.objects.all().order_by('nombre')
    return render(request, 'tatuadores/lista_tatuadores.html', {'tatuadores': tatuadores})


def crear_tatuador(request):
    if request.method == 'POST':
        form = TatuadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tatuadores')
    else:
        form = TatuadorForm()
    return render(request, 'tatuadores/form_tatuador.html', {'form': form, 'titulo': 'Nuevo tatuador'})


def editar_tatuador(request, pk):
    tatuador = get_object_or_404(Tatuador, pk=pk)
    if request.method == 'POST':
        form = TatuadorForm(request.POST, instance=tatuador)
        if form.is_valid():
            form.save()
            return redirect('lista_tatuadores')
    else:
        form = TatuadorForm(instance=tatuador)
    return render(request, 'tatuadores/form_tatuador.html', {'form': form, 'titulo': 'Editar tatuador'})


def eliminar_tatuador(request, pk):
    tatuador = get_object_or_404(Tatuador, pk=pk)
    if request.method == 'POST':
        tatuador.delete()
        return redirect('lista_tatuadores')
    return render(request, 'tatuadores/confirmar_eliminar.html', {'tatuador': tatuador})