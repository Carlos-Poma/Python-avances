#Escribir un programa que le diga al usuario que ingrese una cadena.
#El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
def numero_mayusculas(cadena_texto):
    total = 0
    mayusculas = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    for caracter in mayusculas:
        num_mayusculas = cadena_texto.count(caracter)
        total +=num_mayusculas
    return total



palabra = input("Ingrese una palabra o texto para filtrar las mayusculas")
print(numero_mayusculas(palabra))
