#Escribir una función sum() y una función multip() que sumen y multipliquen 
#respectivamente todos los números de una lista. Por ejemplo:
#sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.


#suma de numeros de una lista
def sum(lista_numeros):
    resultado = 0    
    for numero in lista_numeros: resultado = resultado + numero
    return resultado

#multiplicación de numeros de una lista
def multip(lista_numeros):
    resultado = 1
    for numero in lista_numeros: resultado = resultado * numero 
    return resultado

#resultado de la suma
resultado = sum([1,2,3,4])
print(resultado)
#resultado de la multiplicación
resultado = multip([1,2,3,4])
print(resultado)