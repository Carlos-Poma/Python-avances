#Escribir una función que tome un carácter y devuelva True si es una vocal,
#de lo contrario devuelve False.

def es_vocal(caracter):
    vocales = "aeiou"
    for vocal in vocales:
        if caracter == vocal: return True
    return False

letra = es_vocal("e")
print(letra)