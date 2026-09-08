from django import forms
from .models import Diseno


class DisenoForm(forms.ModelForm):
    class Meta:
        model = Diseno
        fields = ['nombre', 'tatuador_nombre', 'estilo', 'precio', 'tiempo_estimado_horas', 'descripcion']