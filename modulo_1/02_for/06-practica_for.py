
palabra = input("Ingresa una palabra: ")


omitir = {"a", "e", "A", "E"}

resultado_lista = []

for letra in palabra:
    if letra.upper() not in omitir and letra.lower() not in omitir:
        resultado_lista.append(letra)

resultado_final = "".join(resultado_lista)

print(f"Resultado filtrado: {resultado_final}")