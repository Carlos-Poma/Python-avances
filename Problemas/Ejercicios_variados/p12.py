#Escribir una función filtrar_palabras()
#que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(lista,entero):
    for palabra in lista:
        if len(palabra) > entero: print(palabra)

filtrar_palabras(["hola","perro","carlos","paula","gato"],4)