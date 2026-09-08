from django.db import models


class Pago(models.Model):
    METODO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.CharField(max_length=150)
    tatuador = models.CharField(max_length=150)
    servicio = models.CharField(max_length=200, help_text="Descripción del tatuaje o servicio")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES, default='efectivo')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pago = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha_pago']
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return f"{self.cliente} - {self.monto} ({self.estado})"
