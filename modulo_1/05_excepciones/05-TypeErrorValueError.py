def sumar_numeros():
    try:

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        suma = num1 + num2
        return f"La suma es: {suma}"

    except (ValueError, TypeError):

        return "Error: Entrada no válida. Por favor, ingrese solo caracteres numéricos."


# Ejemplo de uso
print(sumar_numeros())
