#Definir una función que calcule la longitud de una lista o una cadena dada.
#(Es cierto que python tiene la función len() incorporada, pero escribirla 
#por nosotros mismos resulta un muy buen ejercicio

def longitud_lista(digitos):
        longitud = 0
        for digito in digitos: longitud+=1
        return longitud

lista = ["Hola",2,4,True,"adios"]

longitud = longitud_lista(lista)
print(longitud)
