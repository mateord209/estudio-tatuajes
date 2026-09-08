from django.db import models


class Diseno(models.Model):
    ESTILOS = [
        ('tradicional', 'Tradicional'),
        ('realismo', 'Realismo'),
        ('blackwork', 'Blackwork'),
        ('acuarela', 'Acuarela'),
        ('minimalista', 'Minimalista'),
    ]

    nombre = models.CharField(max_length=100)
    tatuador_nombre = models.CharField(max_length=100, blank=True)
    estilo = models.CharField(max_length=20, choices=ESTILOS, default='tradicional')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tiempo_estimado_horas = models.DecimalField(max_digits=4, decimal_places=1, default=1)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
