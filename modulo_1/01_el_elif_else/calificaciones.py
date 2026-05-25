# --- Programa de Clasificación de Notas ---


nota = float(input("Ingresa la nota del estudiante (0-100): "))


if nota >= 90:
    resultado = "Excelente"
elif nota >= 70:
    resultado = "Bueno"
elif nota >= 50:
    resultado = "Regular"
else:
    resultado = "Deficiente"

# Mostramos el resultado final
print("------------------------------")
print(f"El desempeño es: {resultado}")
print("------------------------------")