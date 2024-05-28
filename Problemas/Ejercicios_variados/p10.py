#Escribir una función max_in_list()
#que tome una lista de números y devuelva el mas grande.

def max_in_list(lista=[0]):
    lista.sort()
    return lista[-1]

lista = [34,435,5,5,564,67,743,324,32,0]
print(max_in_list(lista))