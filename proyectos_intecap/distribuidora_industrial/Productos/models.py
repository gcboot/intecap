from django.db import models

# Create your models here.
class Producto(models.Model):
  codigo = models.CharField(max_length=10)
  nombre = models.CharField(max_length=100)
  presentacion = models.CharField(max_length=150)
  costo_compra = models.DecimalField(max_digits=10, decimal_places=2)
  precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return self.nombre