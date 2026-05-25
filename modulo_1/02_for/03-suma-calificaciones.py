# -- Ejercicio 3: Suma de calificaciones
# Aquí acumulamos los valores en una variable llamada suma_total
calificaciones = [85, 92, 78, 96, 88]
suma_total = 0

for calificacion in calificaciones:
    suma_total += calificacion

print(f"La suma total de las calificaciones es: {suma_total}")