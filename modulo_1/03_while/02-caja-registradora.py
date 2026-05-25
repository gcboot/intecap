# -- Problema 2: Caja registradora
# Aquí el ciclo se repite pidiendo precios. Se detiene únicamente cuando el cajero ingresa el valor 0


total = 0
precio = -1 # Iniciamos con un valor que permita entrar al ciclo

print("Ingrese los precios de los productos (ingrese 0 para terminar):")

while precio != 0:
    precio = float(input("Precio del producto: "))
    total += precio # Acumulamos el total de la compra [cite: 28]

print(f"El total de la compra es: {total}")