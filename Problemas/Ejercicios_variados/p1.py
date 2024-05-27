#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(*nums):
    lista = [*nums]
    lista.sort()
    return lista[-1]

el_mayor = max(23,22,1,12)
print(el_mayor)
