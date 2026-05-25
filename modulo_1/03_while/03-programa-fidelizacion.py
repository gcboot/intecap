# -- Problema 3: Programa de fidelización
# En este caso, sumamos 10 puntos por cada compra. El programa pregunta al usuario si desea continuar después de cada acumulación.# 



puntos = 0
continuar = "si"

while continuar.lower() == "si":
    puntos += 10 # Acumula 10 puntos por compra 
    print(f"¡Has ganado 10 puntos! Total acumulado: {puntos}")
    
    # Preguntamos si desea seguir comprando 
    continuar = input("¿Desea seguir comprando? (si/no): ")

print(f"Gracias por su visita. Sus puntos finales son: {puntos}")