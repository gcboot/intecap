### Productos/admin.py
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # 7.1. Se divida por columnas: Código, Nombre, Presentación y Precio de venta
    list_display = ['codigo', 'nombre', 'presentacion', 'precio_venta']

    # 7.2. Se permita buscar por: Código, Nombre y Presentación
    search_fields = ['codigo', 'nombre', 'presentacion']

    # 7.3. Se permita filtrar por: Precio de compra y Precio de venta
    list_filter = ['costo_compra', 'precio_venta']

    # 8. Campos en el formulario ordenados de forma específica:
    # Código, Nombre, Precio de venta, Precio de compra y Presentación
    fields = ['codigo', 'nombre', 'precio_venta', 'costo_compra', 'presentacion']

# admin.site.register(Producto, ProductoAdmin)

