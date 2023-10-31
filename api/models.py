from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255, null=False)
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    