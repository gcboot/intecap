# 01 - Importar paquetes

import math, random, requests
from libreria import saludar

# 02 - Usar funciones de los módulos importados

# Raíz cuadrada de 144
raiz_cuadrada = math.sqrt(144)
print(f"La raíz cuadrada de 144 es: {raiz_cuadrada}")

# Generar un número aleatorio entre 1 y 50
numero_aleatorio = random.randint(1, 50)
print(f"El número aleatorio generado es: {numero_aleatorio}")

# 04 - Conexcion a internet con requests python.org
respuesta = requests.get("https://www.python.org")
if respuesta.status_code == 200:
    print("Conexión exitosa a python.org")
else:
    print("Error al conectar a python.org")
    
# 05 - Creacion de propio modulo y uso de su función
nombre_usuario = "Victor"
mensaje_bienvenida = saludar(nombre_usuario)
print(mensaje_bienvenida)
