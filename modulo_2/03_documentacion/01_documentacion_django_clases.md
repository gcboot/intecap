# Documentación Django

1. Crear proyectos nuevos con Django

```shell
mkdir mysite
cd mysite
python -m venv venv
source venv/bin/activate
pip install django
django-admin startproject config .
```

2. Crear aplicaciones (modulos) de django dentro de un proyecto
   
```shell
python manage.py startapp blog
```
3. Crear modelos por medio de clases dentro de aplicaciones (módulos) de Django
   
```python
### 1. models.py dentro de la aplicación blog
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

### 2. Settings.py de config agregaamos la aplicación
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

4. Preparar migraciones en proyectos de Django
```shell
python manage.py makemigrations blog

```

5. Ejecutar migraciones en proyectos de Django
```shell
python manage.py migrate blog
```

6. Entrar a la consola (shell) de Python con Djangopython 

```shell
python manage.py shell
```

7. Crear nuevos registros para modelos creados dentro de aplicaciones (módulos)

```python
### Desde Django shell (python manage.py shell)
from blog.models import Post
from django.contrib.auth.models import User

# Método 1: Crear un usuario primero (si no existe)
user = User.objects.get(username='admin')  # o crea uno nuevo

# Método 2: Crear registro con create()
post = Post.objects.create(
    title="Mi primer post",
    content="Este es el contenido de mi primer post",
    author=user
)

# Método 3: Crear registro con save()
post = Post(
    title="Segundo post",
    content="Contenido del segundo post",
    author=user
)
post.save()

# Método 4: create() con get_or_create() (evita duplicados)
post, created = Post.objects.get_or_create(
    title="Post único",
    defaults={
        'content': "Contenido único",
        'author': user
    }
)

print(f"¿Fue creado? {created}")
```

8. Listar los registros para modelos creados dentro de aplicaciones (módulos)


```python
### Desde Django shell (python manage.py shell)
from blog.models import Post

# Método 1: Obtener todos los registros en un QuerySet
posts = Post.objects.all()
for p in posts:
    print(p.title)

# Método 2: Listar los valores específicos de forma limpia con values()
titulos = Post.objects.values('title', 'date_posted')
print(list(titulos))

# Método 3: Obtener una lista plana de un solo campo con values_list()
lista_titulos = Post.objects.values_list('title', flat=True)
print(list(lista_titulos))

```
9. Modificar registros para modelos creados dentro de aplicaciones (módulos)

```python

### Desde Django shell (python manage.py shell)
from blog.models import Post

# Método 1: Obtener un registro por ID, modificarlo y guardarlo con save()
post = Post.objects.get(id=1)
post.title = "Mi primer post (Editado)"
post.save()

# Método 2: Modificar múltiples registros a la vez con update()
# Nota: Esto se aplica sobre un QuerySet y guarda los cambios inmediatamente
Post.objects.filter(title="Segundo post").update(content="Nuevo contenido para el segundo post")

```

10. Eliminar registros para modelos creados dentro de aplicaciones (módulos)

```python

### Desde Django shell (python manage.py shell)
from blog.models import Post

# Método 1: Obtener un registro específico por ID y eliminarlo
post_a_eliminar = Post.objects.get(id=2)
post_a_eliminar.delete()

# Método 2: Eliminar múltiples registros que cumplan una condición
# ¡Precaución!: Esto borrará todos los registros que coincidan con el filtro
Post.objects.filter(title="Post único").delete()

# Método 3: Eliminar absolutamente TODOS los registros del modelo
# Post.objects.all().delete()

```
11. Filtrar para obtener ciertos registros para modelos creados dentro de aplicaciones (módulos)

```python

### Desde Django shell (python manage.py shell)
from blog.models import Post
from django.contrib.auth.models import User

user = User.objects.get(username='admin')

# Método 1: Filtrar usando coincidencia exacta con filter()
posts_de_admin = Post.objects.filter(author=user)

# Método 2: Filtrar buscando coincidencias parciales (case-insensitive) con __icontains
posts_con_titulo = Post.objects.filter(title__icontains="primer")

# Método 3: Excluir registros que cumplan una condición usando exclude()
posts_no_admin = Post.objects.exclude(author=user)

# Método 4: Encadenar filtros para búsquedas más específicas
posts_especificos = Post.objects.filter(author=user).filter(title__icontains="post")

# Método 5: Obtener un único registro (lanza error si no existe o si hay más de uno)
un_solo_post = Post.objects.get(title="Mi primer post (Editado)")


```






