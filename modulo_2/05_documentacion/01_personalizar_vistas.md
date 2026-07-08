# Personalización de Vistas en el Django Admin

Este documento describe el procedimiento para personalizar la vista de listado de los registros de un modelo específico en Django Admin.

## 1. Personalizar la vista de listado de los registros de un modelo específico, para lograr:

Para personalizar cómo se listan los registros de un modelo en el panel de administración, se define una clase que hereda de `admin.ModelAdmin` y se registra junto con el modelo correspondiente en el archivo `admin.py`.

### Habilitar la edición de los valores de ciertas columnas

La edición rápida en la vista de listado permite a los usuarios modificar valores de campos directamente desde la tabla de registros sin tener que ingresar al formulario de edición detallada de cada registro. Esto se logra mediante el atributo `list_editable`.

#### Requisitos y restricciones:
* Los campos especificados en `list_editable` deben estar presentes también en `list_display` (la lista de columnas a mostrar).
* Los campos en `list_editable` **no** pueden estar configurados como enlaces a la página de edición detallada (es decir, no pueden estar en `list_display_links`). Por defecto, el primer campo en `list_display` es el enlace de edición, por lo que no puede ser editable a menos que se redefina `list_display_links`.

#### Ejemplo de código (Python):

```python
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Definición de las columnas que se mostrarán en el listado
    list_display = ('id', 'nombre', 'precio', 'stock', 'activo')
    
    # Se establece 'nombre' como enlace para evitar conflictos con 'list_editable'
    list_display_links = ('nombre',)
    
    # Habilita la edición directa en la tabla de listado para precio, stock y activo
    list_editable = ('precio', 'stock', 'activo')
```

---

### Definir funciones para acciones y registrarlas para que se puedan ejecutar con los registros seleccionados

Las acciones personalizadas permiten realizar operaciones masivas sobre un conjunto de registros seleccionados en la vista de lista del administrador.

#### Procedimiento para crear y registrar una acción:
1. **Definir la función de la acción:**
   La función debe recibir tres argumentos:
   * `modeladmin`: La clase `ModelAdmin` actual.
   * `request`: El objeto HTTP que representa la petición actual (`HttpRequest`).
   * `queryset`: El conjunto de registros seleccionados por el usuario.
2. **Definir una descripción:**
   Se utiliza el decorador `@admin.action(description="Texto descriptivo")` para especificar la etiqueta que se mostrará en el menú desplegable de acciones.
3. **Registrar la acción:**
   Se agrega la referencia a la función de acción dentro de la lista o tupla `actions` de la clase `ModelAdmin`.

#### Ejemplo de código (Python):

```python
from django.contrib import admin
from django.contrib import messages
from .models import Producto

# 1. Definición de la función de acción personalizada
@admin.action(description="Marcar productos seleccionados como activos")
def activar_productos(modeladmin, request, queryset):
    # Actualiza el campo activo a True para todos los registros seleccionados
    actualizados = queryset.update(activo=True)
    
    # Envía un mensaje de éxito al usuario
    modeladmin.message_user(
        request, 
        f"Se han activado {actualizados} producto(s) correctamente.", 
        messages.SUCCESS
    )

# 2. Registro de la acción en la clase de administración
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'activo')
    list_display_links = ('nombre',)
    list_editable = ('precio', 'stock', 'activo')
    
    # Registrando la acción personalizada
    actions = [activar_productos]
```

---

## 2. Comandos útiles de terminal

Para ejecutar el servidor local y aplicar cambios en el administrador, utilice los siguientes comandos:

```bash
# Iniciar el servidor de desarrollo de Django
python manage.py runserver
```

Si se requiere realizar migraciones de base de datos antes de visualizar los cambios:

```bash
# Detectar y preparar los cambios en los modelos
python manage.py makemigrations

# Aplicar los cambios a la base de datos
python manage.py migrate
```