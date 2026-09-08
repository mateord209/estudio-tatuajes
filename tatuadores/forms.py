from django import forms
from .models import Tatuador


class TatuadorForm(forms.ModelForm):
    class Meta:
        model = Tatuador
        fields = ['nombre', 'especialidad', 'telefono', 'anios_experiencia', 'activo']