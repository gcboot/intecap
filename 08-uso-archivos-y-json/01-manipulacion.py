# 01 - Leer archivo
import os

directorio_actual = os.path.dirname(__file__)


ruta_archivo = os.path.join(directorio_actual, "clientes.txt")

try:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en: {ruta_archivo}")


# 02 - Escribir (Añadir) en un archivo existente
directorio_actual2 = os.path.dirname(__file__)
ruta_archivo2 = os.path.join(directorio_actual2, "ventas.txt")

try:

    with open(ruta_archivo2, "a", encoding="utf-8") as archivo:

        archivo.write("\nVenta Realizada: Libro de Python")

    print(f"Se ha añadido información a 'ventas.txt' en: {ruta_archivo2}")
except Exception as e:
    print(f"Error al escribir en el archivo: {e}")
