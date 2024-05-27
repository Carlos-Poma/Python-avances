#Variables a usar
lista_1 = list(["Hola","Carlos",24])# <-- Creado con list()

#len() <-- Devuelve la cantidad de elementos de la lista
#         ----- len() es una función ------
cantidad_elementos = len(lista_1)
print(cantidad_elementos)#3

# append <-- agrega elementos a la lista
#agrega elementos a la lista original no a la nueva variable
#agregar_elementos_append = lista_1.append(2) <-- no es necesario una nueva variable
lista_1.append(2)
#como agrega a la lista original, llamamos a la variable original "lista_1"
print(lista_1)#['Hola', 'Carlos', 34, 2]

#insert <-- agrega un elemento a la lista en un indice especifico
# insert(indice, parametro) <-- el parametro es lo nuevo a agregar
lista_1.insert(2, "Poma")
print(lista_1)#['Hola', 'Carlos', 'Poma', 24, 2]

#extend() <-- agrega varios elementos a la lista de otra lista
#           ------- extend(["lista_a_agregar"]) -------
lista_1.extend([20, True, "Motivado"])# <-- se tiene que agregar una lista
print(lista_1)#['Hola', 'Carlos', 'Poma', 24, 2, 20, True, 'Motivado']

#pop() <-- elimina un elemento de la lista por su indice
# un truco para eliminar el ultimo elemento es colocar el indice -1
lista_1.pop(3)# lista.pop(indice)
print(lista_1)#['Hola', 'Carlos', 'Poma', 2, 20, True, 'Motivado']

#remove() <-- elimina un elemento por su valos
lista_1.remove(2)# <-- 2 es un elemonto no un indice 
print(lista_1)#['Hola', 'Carlos', 'Poma', 20, True, 'Motivado']

#sort() <-- ordena los elementos de forma ascendente
#no se puede ordenar listas que tengran strings
lista_2 = [23, 123, 12, 32, 4, 45, 77, 0, True, False]
#lista_1.sort() <-- esto dara un error por que tiene cadenas de texto
lista_2.sort()# <-- entre False y True, los False son primeros
#    sort() <-- se le puede dar el parametro reverse --> sort(reverse = True)
print(lista_2)#[0, False, True, 4, 12, 23, 32, 45, 77, 123]

#reverse() <-- XD reverse tambien es un metodo 
#reverse() <-- invierte los elementos de la lista
lista_2.reverse()
print(lista_2)#[123, 77, 45, 32, 23, 12, 4, True, False, 0]

#index <-- verificando si un elemento se encuentra en la lista 
elemento_encontrado = lista_2.index(12)
print(elemento_encontrado)#5










#clear() <-- elimina todos los elementos de la lista