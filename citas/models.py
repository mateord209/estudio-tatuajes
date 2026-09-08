from django.db import models


class Cita(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('realizada', 'Realizada'),
    ]

    nombre_cliente = models.CharField(max_length=100)
    nombre_tatuador = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion_diseno = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha} {self.hora}"