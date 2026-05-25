🚀 INTECAP - Programación en Python

Este repositorio contiene una colección de guías, hojas de trabajo, ejemplos y proyectos prácticos desarrollados durante el curso de formación en **INTECAP** (Instituto Técnico de Capacitación y Productividad). El objetivo principal de este espacio es documentar y estructurar el progreso en el aprendizaje de lógica de programación, algoritmos, manipulación de datos, control de excepciones, Programación Orientada a Objetos (POO), y persistencia de datos en Python 3.x.

---

## 📂 Estructura del Proyecto

El repositorio está organizado de forma modular, permitiendo navegar desde los conceptos más básicos de control de flujo hasta proyectos consolidados en consola:

```text
intecap/
├── modulo_1/                     # Ejercicios y proyectos del primer módulo
│   ├── 01_el_elif_else/          # Estructuras de control condicional (if-elif-else)
│   ├── 02_for/                   # Estructuras de control iterativas (Ciclo for)
│   ├── 03_while/                 # Ciclo while y control de flujo basado en condiciones
│   ├── 04_listas/                # Manejo de colecciones, arrays y manipulación de listas
│   ├── 05_excepciones/           # Control de errores y robustez de código (try-except)
│   ├── 06_poo/                   # Clases, objetos, herencia, encapsulamiento y polimorfismo
│   ├── 07_modulos_paquetes/      # Modularización de código e importación de bibliotecas
│   ├── 08_uso_archivos_y_json/   # Lectura/escritura de archivos planos y serialización JSON
│   └── 09_proyecto_modulo_uno/   # Proyecto Final del Módulo 1 (Sistema "Abundancia")
├── modulo_2/                     # Reservado para contenidos de la siguiente etapa
└── README.md                     # Documentación principal del repositorio
```

---

## 📖 Detalles de los Módulos

### 🔷 Módulo 1: Fundamentos y Programación Orientada a Objetos
En este módulo se sientan las bases sólidas de la programación imperativa y estructurada en Python, culminando con la implementación del paradigma orientado a objetos y persistencia local de datos.

| Directorio | Temática Principal | Ejercicios Destacados |
| :--- | :--- | :--- |
| [01_el_elif_else](file:///Users/victorcun/projects/learning/intecap/modulo_1/01_el_elif_else) | Condicionales y toma de decisiones | Control de calificaciones (`calificaciones.py`) |
| [02_for](file:///Users/victorcun/projects/learning/intecap/modulo_1/02_for) | Bucles determinados e iteraciones | Generador de boletos numerados, tablas de multiplicar, conteo de palabras, acumulador de calificaciones |
| [03_while](file:///Users/victorcun/projects/learning/intecap/modulo_1/03_while) | Bucles indeterminados y menús interactivos | Control de inventario, simulación de caja registradora, programas de fidelización |
| [04_listas](file:///Users/victorcun/projects/learning/intecap/modulo_1/04_listas) | Estructuras de datos lineales y mutabilidad | Simulación de inventario y precios para Abarrotería "El Buen Vecino" |
| [05_excepciones](file:///Users/victorcun/projects/learning/intecap/modulo_1/05_excepciones) | Control de errores y flujos alternativos | Manejo de excepciones comunes (`ZeroDivisionError`, `IndexError`, `TypeError`, `ValueError`) |
| [06_poo](file:///Users/victorcun/projects/learning/intecap/modulo_1/06_poo) | Programación Orientada a Objetos (POO) | Creación de clases (`Libro`), Herencia (`Empleado` y `Gerente`), Encapsulamiento, Polimorfismo y sistema de Gestión Escolar |
| [07_modulos_paquetes](file:///Users/victorcun/projects/learning/intecap/modulo_1/07_modulos_paquetes) | Reutilización de código y modularización | Importación de paquetes internos (`math`, `random`), librerías externas (`requests`) y diseño de módulos propios |
| [08_uso_archivos_y_json](file:///Users/victorcun/projects/learning/intecap/modulo_1/08_uso_archivos_y_json) | Persistencia local de información | Lectura y adición en archivos planos (`clientes.txt`, `ventas.txt`) |
| [09_proyecto_modulo_uno](file:///Users/victorcun/projects/learning/intecap/modulo_1/09_proyecto_modulo_uno) | Consolidación y desarrollo práctico | **Proyecto "Abundancia"**: Sistema CLI integral de gestión de clientes. Aplica POO, validación avanzada de datos con expresiones regulares (regex) y persistencia/sincronización dinámica de archivos planos. |

### 🔶 Módulo 2: Siguiente Etapa
*Espacio preparado para la continuación del plan de estudios de INTECAP.*

---

## 🛠️ Tecnologías y Herramientas

- **Lenguaje:** [Python 3.x](https://www.python.org/)
- **Entorno de Desarrollo:** Visual Studio Code / PyCharm / Terminal de comandos
- **Bibliotecas Utilizadas:**
  - Estándar: `os`, `re`, `math`, `random`
  - Externas: `requests`

---

## 🚀 Configuración y Ejecución

Sigue estos pasos para clonar el repositorio e interactuar con los ejercicios de forma segura utilizando un entorno virtual (`venv`):

### 1. Clonar el repositorio
```bash
git clone <url_del_repositorio>
cd intecap
```

### 2. Crear y activar el entorno virtual
El repositorio ya cuenta con una carpeta `venv` preconfigurada (excluida en el control de versiones por `.gitignore`), pero puedes volver a crearla o activarla según tu sistema:

- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

### 3. Instalar dependencias necesarias
Para ejecutar los ejemplos de conexiones de red (por ejemplo, en el módulo 7):
```bash
pip install requests
```

### 4. Ejecutar el proyecto principal
Para probar la aplicación interactiva del final del módulo 1 (gestión de cartera de clientes "Abundancia"):
```bash
python modulo_1/09_proyecto_modulo_uno/abundacia.py
```

---

> [!NOTE]
> Todos los ejercicios y hojas de trabajo en formato PDF adjuntos corresponden a las guías de estudio teóricas y prácticas oficiales provistas por INTECAP, resueltas de manera individual.