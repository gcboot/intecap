# Guía de Django: Entornos Virtuales, Instalación y Primer Proyecto

Este documento contiene las guías detalladas para preparar tu entorno de desarrollo, instalar Django y poner en marcha tu primer proyecto.

---

## 1. Guía de creación de entornos virtuales en una carpeta específica

Un entorno virtual es un espacio aislado que permite instalar paquetes y dependencias de Python para un proyecto en particular sin interferir con otros proyectos o la instalación global de Python.

### Paso 1: Abrir la terminal o línea de comandos
Navega mediante la terminal hasta la carpeta específica en la que deseas trabajar o donde estará tu proyecto.
*(Ejemplo: `/Users/tu_usuario/projects/mi_proyecto`)*

### Paso 2: Crear el entorno virtual
Ejecuta el siguiente comando para crear un entorno virtual utilizando el módulo integrado `venv` de Python. Puedes especificar la ruta o nombre de la carpeta donde se creará el entorno:

- **En la carpeta actual (recomendado si ya estás dentro de la carpeta del proyecto):**
  ```bash
  python3 -m venv .venv
  ```
  *(Nota: En Windows puedes usar `python` en lugar de `python3`)*

- **En una carpeta específica o con un nombre personalizado:**
  ```bash
  python3 -m venv /ruta/a/tu/carpeta/mi_entorno
  ```

### Paso 3: Activar el entorno virtual
Antes de instalar cualquier paquete, debes activar el entorno virtual.

- **En macOS y Linux:**
  ```bash
  source .venv/bin/activate
  ```
  *O si usaste una ruta específica:*
  ```bash
  source /ruta/a/tu/carpeta/mi_entorno/bin/activate
  ```

- **En Windows (Command Prompt - cmd):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

- **En Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

Una vez activado, verás el nombre del entorno entre paréntesis al inicio de la línea de comandos, por ejemplo: `(.venv) user@machine:~$`.

### Paso 4: Desactivar el entorno virtual (cuando termines de trabajar)
Para salir del entorno virtual y volver al entorno global del sistema, simplemente ejecuta:
```bash
deactivate
```

---

## 2. Guía de instalación de Django en un entorno virtual

Una vez que tengas tu entorno virtual creado y **activo**, puedes proceder a instalar Django de forma aislada.

### Paso 1: Asegurar que el entorno virtual está activo
Verifica que aparezca `(.venv)` (o el nombre de tu entorno) al inicio de la línea de tu terminal.

### Paso 2: Actualizar `pip` (Opcional pero recomendado)
Es buena práctica asegurarse de tener la última versión del gestor de paquetes de Python:
```bash
pip install --upgrade pip
```

### Paso 3: Instalar Django
Instala la última versión estable de Django usando `pip`:
```bash
pip install django
```

*Si deseas instalar una versión específica de Django (por ejemplo, la versión 4.2 LTS), puedes indicarla de la siguiente manera:*
```bash
pip install django==4.2
```

### Paso 4: Verificar la instalación
Comprueba que Django se ha instalado correctamente ejecutando:
```bash
python -m django --version
```
Esto debería mostrar la versión instalada (por ejemplo, `5.0.6`).

![Instalación y creación de Django](instlacion%20y%20creacion.png)

---

## 3. Guía de creación de un nuevo proyecto de Django y ejecución del servidor web de desarrollo

Con Django instalado en tu entorno virtual activo, ya estás listo para crear tu estructura de proyecto y ejecutar el servidor de desarrollo local.

### Paso 1: Crear el proyecto Django
Decide si quieres que Django cree una nueva carpeta para el proyecto o si prefieres crearlo en la carpeta actual.

- **Opción A: Crear el proyecto en la carpeta actual (Recomendado)**
  Si ya estás dentro de la carpeta raíz de tu repositorio/proyecto y no quieres crear una subcarpeta adicional con el mismo nombre, usa un punto `.` al final:
  ```bash
  django-admin startproject mi_proyecto .
  ```
  *Esto creará el archivo `manage.py` en la carpeta actual y la carpeta de configuración `mi_proyecto`.*

- **Opción B: Crear una nueva carpeta para el proyecto**
  Si deseas que Django cree una subcarpeta nueva con el nombre del proyecto:
  ```bash
  django-admin startproject mi_proyecto
  ```
  *Luego, deberás entrar a la carpeta recién creada antes de continuar:*
  ```bash
  cd mi_proyecto
  ```

### Paso 2: Comprender la estructura generada
El comando anterior creará una estructura similar a la siguiente:
```text
mi_proyecto/         <-- Carpeta raíz del proyecto
├── manage.py        <-- Utilidad de línea de comandos para interactuar con el proyecto
└── mi_proyecto/     <-- Paquete de Python con la configuración
    ├── __init__.py
    ├── settings.py  <-- Configuración principal del proyecto
    ├── urls.py      <-- Declaración de URLs/Rutas
    ├── asgi.py      <-- Configuración para servidores web asíncronos (ASGI)
    └── wsgi.py      <-- Configuración para servidores web síncronos (WSGI)
```

### Paso 3: Realizar las migraciones iniciales (Opcional pero recomendado)
Django viene por defecto con algunas aplicaciones preinstaladas (como la administración, autenticación, etc.) que requieren tablas en la base de datos. Crea estas tablas con:
```bash
python manage.py migrate
```

### Paso 4: Ejecutar el servidor web de desarrollo
Inicia el servidor local de desarrollo integrado en Django ejecutando:
```bash
python manage.py runserver
```

Si deseas ejecutar el servidor en un puerto diferente (por ejemplo, el puerto `8080`), puedes especificarlo al final:
```bash
python manage.py runserver 8080
```

### Paso 5: Probar en el navegador web
Una vez iniciado el servidor, verás un mensaje indicando que está corriendo. Abre tu navegador web favorito y accede a la siguiente dirección:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) o [http://localhost:8000/](http://localhost:8000/)

Deberías ver la página de bienvenida predeterminada de Django con un cohete despegando y el mensaje *"The install worked successfully! Congratulations!"*.

![Servidor de Django corriendo](django%20corriendo.png)

Para detener el servidor en cualquier momento, presiona `Ctrl + C` en tu terminal.
