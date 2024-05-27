#forma no optima de sumar valores
#def suma(lista):
#     numeros_sumados = 0
#     for numeros in lista:
#         numeros_sumados = numeros_sumados + numeros
#     return numeros_sumados

#resultado = suma([5,3,9])

#Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado = suma_total([5,3,9])
print(resultado)

#Utilizando el operador * como argumento (args)
def suma(nombre, *numeros):
   return f'{nombre}, la suma de tus numeros es {sum(numeros)}'

resultado = suma("Carlos",5,6,7)
print(resultado)

