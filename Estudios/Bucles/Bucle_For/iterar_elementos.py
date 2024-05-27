
animales = ["gato", "perro", "loro", "cocodrilo", "pez"]
numeros = [10, 12, 34, 45, 70]

#recorre la lista de animales
for animal in animales:
    print(f'Ahora vale: {animal}')

#recorriendo la lista de numeros y multiplicando cada valor por 10
for numero in numeros:
    print(f'Ahora el número vale: {numero}')
    resultado = numero * 10
    print(f'La multiplicación del número actual por 10 es {resultado}')

#iterando 2 listas al mismo tiempo
for animal, numero in zip(animales, numeros):
    print(f'recorriendo  lista 1: {animal}')
    print(f'recorriendo  lista 2: {numero}')

#forma no optima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#form correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'Indice es: {indice} y el valor: {valor}')

# for num, i in enumerate(numeros):
#     print(num, i)


#usando el else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("El bucle termino")




















   
# lado = int(input("ingresa las dimenciones del cuadrado: "))
# lista = []
# for fila in range(lado): 
#     for columna in range(lado):
#         lista.insert(columna, "*")
#         print(lista[columna], end="")
#     print("")
