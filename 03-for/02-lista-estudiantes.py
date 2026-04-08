# -- Ejercicio 2: Lista de estudiantes
# Para este usamos la lista que te dieron y una variable contador para el número de lista.

estudiantes = ["Ana", "Luis", "María", "José"]
no_lista = 1

for nombre in estudiantes:
    print(f"{no_lista}. {nombre}")
    no_lista += 1  # Sumamos 1 en cada vuelta