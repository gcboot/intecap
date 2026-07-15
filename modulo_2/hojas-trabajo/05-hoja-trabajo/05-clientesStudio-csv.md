# Caso: Exportación CSV en Módulo de Clientes para Studio M

Este documento detalla la modificación del módulo de clientes existente para incorporar nombres detallados (*verbose names*) formateados según los requisitos de **Studio M**, así como una acción personalizada en el sitio administrativo para exportar los registros de clientes seleccionados en formato CSV.

---

## 📋 Requisitos Previos e Inicialización

### 1. Activar el entorno virtual del proyecto
Antes de comenzar, asegúrate de situarte en la carpeta raíz del proyecto de **Studio M** y activar el entorno virtual correspondiente:

**En Windows (PowerShell/CMD):**
```bash
venv\Scripts\activate
```

**En macOS/Linux (Terminal):**
```bash
source venv/bin/activate
```

---

## 🛠️ Instrucciones de Implementación

### 5. Configurar Nombres Detallados en el Modelo (*Verbose Names*)
Para garantizar que los campos del modelo `Cliente` se muestren con el formato de texto y mayúsculas requerido en las vistas de lista y formulario de Django, actualiza el archivo `clientes/models.py`.

Modifica el archivo `clientes/models.py` agregando la propiedad `verbose_name` a cada campo como se detalla a continuación:

```python
# clientes/models.py
from django.db import models

class Cliente(models.Model):
    # 5.1. DPI (En mayúsculas)
    dpi = models.CharField(
        max_length=13, 
        unique=True, 
        verbose_name="DPI"
    )

    # 5.2. Nombres (Inicial mayúscula)
    nombres = models.CharField(
        max_length=100, 
        verbose_name="Nombres"
    )

    # 5.3. Apellidos (Inicial mayúscula)
    apellidos = models.CharField(
        max_length=100, 
        verbose_name="Apellidos"
    )

    # 5.4. Fecha de nacimiento
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de nacimiento"
    )

    # 5.5. Teléfono (Inicial mayúscula)
    telefono = models.CharField(
        max_length=15, 
        verbose_name="Teléfono"
    )

    # 5.6. Dirección de residencia
    direccion = models.CharField(
        max_length=100, 
        verbose_name="Dirección de residencia"
    )

    # 5.7. Dirección de correo electrónico
    correo_electronico = models.EmailField(
        max_length=100, 
        verbose_name="Dirección de correo electrónico"
    )

    # 5.8. Activo (Inicial mayúscula)
    activo = models.BooleanField(
        default=True, 
        verbose_name="Activo"
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.dpi})"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
```

---

### 6. Agregar Acción de Exportación a CSV en el Panel de Administración
Para permitir la descarga de los clientes seleccionados en un archivo plano CSV, debemos registrar la acción personalizada en la clase de administración del modelo `Cliente`.

Modifica el archivo `clientes/admin.py` incorporando la función `exportar_a_csv` y asegurándote de conservar las acciones previas de activación/inactivación:

```python
# clientes/admin.py
import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Cliente

# 6.1. Acción personalizada para exportar a CSV
@admin.action(description='Exportar registros seleccionados a CSV')
def exportar_a_csv(modeladmin, request, queryset):
    # Definimos el tipo de contenido para la respuesta HTTP
    response = HttpResponse(content_type='text/csv')
    
    # Forzamos la descarga del archivo con el nombre especificado
    response['Content-Disposition'] = 'attachment; filename="clientes_studio_m.csv"'

    writer = csv.writer(response)
    
    # Escribimos los encabezados de las columnas en el CSV
    writer.writerow([
        'DPI', 
        'Nombres', 
        'Apellidos', 
        'Fecha de nacimiento', 
        'Teléfono', 
        'Dirección de residencia', 
        'Dirección de correo electrónico', 
        'Activo'
    ])

    # Recorremos los registros seleccionados y escribimos sus datos
    for cliente in queryset:
        writer.writerow([
            cliente.dpi,
            cliente.nombres,
            cliente.apellidos,
            cliente.fecha_nacimiento,
            cliente.telefono,
            cliente.direccion,
            cliente.correo_electronico,
            cliente.activo
        ])

    return response


# Acciones previas (se mantienen en el sistema)
@admin.action(description='Inactivar los clientes seleccionados')
def inactivar_clientes(modeladmin, request, queryset):
    queryset.update(activo=False)


@admin.action(description='Activar los clientes seleccionados')
def activar_clientes(modeladmin, request, queryset):
    queryset.update(activo=True)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dpi', 'nombres', 'apellidos', 'telefono', 'activo')
    search_fields = ('dpi', 'nombres', 'apellidos', 'telefono')
    list_filter = ('fecha_nacimiento', 'activo')
    list_editable = ('nombres', 'apellidos', 'telefono')

    # Agregamos la nueva acción a la lista de acciones disponibles
    actions = [inactivar_clientes, activar_clientes, exportar_a_csv]


# Registro del modelo con su respectiva clase de administración
admin.site.register(Cliente, ClienteAdmin)
```

> [!TIP]
> Recuerda aplicar las migraciones de Django si realizaste modificaciones en los campos del modelo `Cliente` ejecutando `python manage.py makemigrations` y luego `python manage.py migrate`.
