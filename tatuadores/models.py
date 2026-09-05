from django.db import models


class Tatuador(models.Model):
    ESPECIALIDADES = [
        ('tradicional', 'Tradicional'),
        ('realismo', 'Realismo'),
        ('blackwork', 'Blackwork'),
        ('acuarela', 'Acuarela'),
        ('minimalista', 'Minimalista'),
    ]

    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDADES, default='tradicional')
    telefono = models.CharField(max_length=20, blank=True)
    anios_experiencia = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre