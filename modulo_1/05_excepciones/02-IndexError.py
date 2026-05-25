def consultar_nota(lista_notas, indice):
    try:

        nota = lista_notas[indice]
        return f"La nota en el índice {indice} es: {nota}"
    except IndexError:

        return f"Error: El índice {indice} no existe en la lista de notas."


notas = [85, 90, 78]
print(consultar_nota(notas, 5))
