from django import forms
from .models import Pago


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['cliente', 'tatuador', 'servicio', 'monto', 'metodo_pago', 'estado', 'observaciones']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'tatuador': forms.TextInput(attrs={'class': 'form-control'}),
            'servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }