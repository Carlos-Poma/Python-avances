# Definir una función superposicion() que tome dos listas 
#y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
#Escribir la función usando el bucle for anidado.

def  superpocición(lista_1,lista_2):
    for elemento1 in lista_1 :
        for elemento2 in lista_2:
            if elemento1 == elemento2 : return True
    return False

lista1 = [1,2,3,4,5,6,7,8]
lista2 = [0,9,10,16]
numero_comun = superpocición(lista1,lista2)
print(numero_comun)