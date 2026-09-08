from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_cliente', 'nombre_tatuador', 'fecha', 'hora', 'descripcion_diseno', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'descripcion_diseno': forms.Textarea(attrs={'rows': 3}),
        }