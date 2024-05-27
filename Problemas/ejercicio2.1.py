#falto el profesor y chicos van a dar la clase

#función para obtener el nombre y la edad de los estudiantes
def cantidad_compañeros(cantidad):
    compañeros = []#lista de estudiantes
    for i in range(cantidad):#tomamos el parametro de cantidad para sabes cuantos estudiantes hay
        nombre = input("Ingrese el nombre del compañero: ")#preguntamos el nombree
        edad = int(input("Ingrese la edad del compañero: "))#preguntamos la edad
        compañero = (nombre,edad)#lo almacenamos en una tupla
        compañeros.append(compañero)#añadimos los compañeros en la lista
    compañeros.sort(key=lambda x:x[1])#ordenamos la lista 
    asistente = compañeros[0][0]#encontramos al menor para asignarle de asistente
    profesor = compañeros[-1][0]#encontramos al mayor para asignarle de profesor
    return asistente, profesor, compañeros#retornamos los datos

#Llamamos a la función 
asistente, profesor, compañeros = cantidad_compañeros(2)#desempaquetamos los datos de ta función

#Mostramos los valores
print(compañeros)
print(f"El profesor es: {profesor}")
print(f"El asistente es: {asistente}")
















# numero_compañeros = int(input("Cuantos alumnos asistierón hoy a clase: "))
# lista_alumnos = cantidad_compañeros(numero_compañeros)
# print(lista_alumnos)

























#Pedimos la edad de todos los alumnos y los colocamos en una lista
# lista_alumnos_edades = []
# for compañeros in range(numero_compañeros):
#     edad = int(input(f"Ingrese la edad del compañero número {compañeros + 1}: "))
#     lista_alumnos_edades.append(edad)
# lista_alumnos_edades.sort()
# #El tiene mayor edad
# profesor = lista_alumnos_edades[-1]
# #El tiene menor edad
# asistente = lista_alumnos_edades[0]

# #Lista de edades de alumnos
# print(lista_alumnos_edades)
# #Mostramos los alumnos que seran el profesor y el asistente
# print(f'El alumno que sera el profesor tiene {profesor} años y el asistente tiene {asistente} años')
