def calcular_cociente(dividendo, divisor):
    try:

        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:

        return "Error: No es posible dividir entre cero."


print(calcular_cociente(10, 0))
