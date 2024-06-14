
# Escribe un programa que cuente el número de vocales en una cadena dada.

palabra = input('Escribe una palabra: ')
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def contar_vocales(palabra, indice=0, contador=0):
    # Caso base
    if indice == len(palabra):
        return contador
    if palabra[indice] in vocales:
        contador += 1
    return contar_vocales(palabra, indice + 1, contador)

numero_de_vocales = contar_vocales(palabra)
print(f"Número de vocales en '{palabra}': {numero_de_vocales}")

