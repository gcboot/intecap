# ==========================================
# ESTUDIO DE CASO: ABARROTERÍA "EL BUEN VECINO"
# ==========================================

# --- Ejercicio 1: Productos ---
# Definimos la lista inicial de artículos [cite: 39]
productos = ["Arroz", "Frijol", "Azúcar", "Aceite", "Sal"]
# Respuesta: Accedería al tercer producto con productos[2] [cite: 46]

# --- Ejercicio 2: Precios ---
# Definimos los precios correspondientes en Quetzales [cite: 48]
precios = [12, 18, 10, 25, 5]
# Respuesta: El precio del aceite se obtiene con precios[3] [cite: 55]

# --- Ejercicio 3: Inventario ---
# Definimos las cantidades disponibles [cite: 57]
inventario = [20, 15, 30, 10, 50]

# Actualización: Se vendieron 5 unidades de azúcar (índice 2) [cite: 64]
inventario[2] = inventario[2] - 5

# --- Ejercicio 4: Operaciones con listas ---
# 1. Agregamos Café
productos.append("Café")
precios.append(15)  # Agregamos un precio para el café
inventario.append(10)  # Agregamos cantidad para el café

# 2. Eliminamos Sal
# Nota: Si eliminamos de productos, también deberíamos quitar de las otras listas
# para no perder la relación de los índices.
productos.remove("Sal")
precios.pop(4)  # Quitamos el precio de la Sal (estaba en el índice 4)
inventario.pop(4)  # Quitamos el inventario de la Sal

# 3. Ordenamos precios (Ojo: esto rompe la relación con productos, pero se pide en el ejercicio) [cite: 69]
precios.sort()

# 4. Total en inventario [cite: 70]
total_productos = sum(inventario)
print(f"Total de productos en inventario: {total_productos}")

# --- Ejercicio 5: Relación y Reporte ---
# Mensaje específico del Frijol usando índices [cite: 75]
print(
    f"El precio del {productos[1]} es {precios[1]} y hay {inventario[1]} unidades en inventario"
)

# Programa que muestra todo el inventario mediante un ciclo [cite: 76]
print("\n--- REPORTE GENERAL DE VENTAS ---")
for i in range(len(productos)):
    print(
        f"Producto: {productos[i]} | Precio: Q{precios[i]} | Cantidad: {inventario[i]}"
    )
