# Documentación del Administrador de Django

Esta guía resume las tareas más comunes del panel administrativo de Django: crear superusuarios, iniciar sesión, administrar usuarios y grupos, registrar modelos y personalizar el listado y los formularios de administración.

---

## 1. Crear un superusuario para el sitio administrativo de Django

Antes de crear el usuario administrador, asegúrate de haber aplicado las migraciones iniciales del proyecto.

```bash
python manage.py migrate
```

Luego crea el superusuario:

```bash
python manage.py createsuperuser
```

El sistema pedirá:

- Nombre de usuario
- Correo electrónico
- Contraseña

---

## 2. Acceder al sitio administrativo de Django

1. Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

2. Abre el navegador y entra a:

```text
http://127.0.0.1:8000/admin/
```

3. Inicia sesión con el superusuario creado.

---

## 3. Crear usuarios y grupos usando el sitio administrativo de Django

Una vez dentro del panel de administración:

1. Entra en **Users** para crear usuarios.
2. Entra en **Groups** para crear grupos.

### 3.1 Crear un usuario

- Haz clic en **Add user**.
- Completa los campos solicitados.
- Guarda el registro.
- En la siguiente pantalla asigna permisos, estado activo y pertenencia a grupos.

### 3.2 Crear un grupo

- Haz clic en **Add group**.
- Escribe el nombre del grupo.
- Asigna permisos al grupo.
- Guarda los cambios.

---

## 4. Registrar en el sitio administrativo de Django un modelo creado dentro de una Django App

Para que un modelo aparezca en el admin, primero debes importarlo y registrarlo en `admin.py` de la app.

### Ejemplo de modelo (`blog/models.py`)

```python
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
```

### Registro del modelo (`blog/admin.py`)

```python
from django.contrib import admin
from .models import Post


admin.site.register(Post)
```

### Activar la app

Verifica que la app esté agregada en `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

---

## 5. Personalizar la vista de listado de registros de un modelo específico

Para controlar cómo se muestra un modelo en el admin, se crea una clase `ModelAdmin`.

### 5.1 Mostrar datos como columnas

Usa `list_display` para mostrar campos como columnas:

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
```

### 5.2 Habilitar búsqueda en determinados campos

Usa `search_fields` para permitir búsquedas:

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')
```

### 5.3 Habilitar filtrado por determinados campos

Usa `list_filter` para agregar filtros laterales:

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('title',)
```

---

## 6. Personalizar un formulario de creación o modificación de un modelo específico

Para definir qué campos se muestran y en qué orden, usa `fields` dentro de `ModelAdmin`.

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('title',)
    fields = ('title', 'content')
```

Si quieres cambiar el orden de los campos, solo modifica la tupla:

```python
fields = ('content', 'title')
```

---

## 7. Ejemplo completo de `admin.py`

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('title',)
    fields = ('title', 'content')
```

---

## 8. Resumen de comandos útiles

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
