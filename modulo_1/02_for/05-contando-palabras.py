# -- Ejercicio 5: Contando palabras
# Para contar palabras en una frase, primero la "rompemos" en pedazos usando .split() y luego los contamos con el ciclo.


frase = "La programación es divertida"
palabras = frase.split() # Esto crea una lista: ["La", "programación", "es", "divertida"]
contador = 0

for palabra in palabras:
    contador += 1

print(f"La frase tiene {contador} palabras.")