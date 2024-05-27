#variables para aplicar metodos
cadena_1 = "Hola soy Carlos"
cadena_2 = "Bienvenido"
cadena_3 = "123123"

# dir() <-- devuelve la lista de atributos validos del objeto pasado
# dir no es un metodo es una función
# print(dir(cadena_1))

#LOS METODOS FUNCIONAN DE LA SIGUIENTE FORMA:
#       ----- variable.metodo() -------


#upper() <-- coloca todo en mayusculas 
mayuscula = cadena_1.upper()
print(mayuscula) #HOLA SOY CARLOS

#lower() <-- coloca todo en minusculas 
minuscula = cadena_1.lower()
print(minuscula) #hola soy carlos

#capitalize() <-- convierte la primera letra en mayuscula
primera_letra = cadena_1.capitalize() # <-- variable con snake_case
print(primera_letra) #Hola soy carlos

#find() <-- busca una cadena en otra cadena
#  retorna la primera posición en la que encuentre una coincidencia
busqueda_find = cadena_1.find("a")# <-- si no encuentra una coincidencia devuleve -1
print(busqueda_find) #3

#index() <-- busca una cadena en otra cadena
# retorna la posición
# si no encuentra una coincidencia devuelve devuelve un error (exeption)
busqueda_index = cadena_1.index("a")# <---^'
print(busqueda_index)#3

#isnumeric() <-- si es numerico, devuelve True, sino devuelve False
es_numerico = cadena_3.isnumeric()
print(es_numerico)#True

#isalpha <-- si es alfanumerico devolvemos True, sino False
es_alfanumerico = cadena_2.isalpha()#solo son validos caracteres de la a-z
print(es_alfanumerico)#True

#count() <-- busca una cadena en otra cadena
#  retorna la cantidad de veces que encuentre una coincidencia
busqueda_count = cadena_1.count("a")# <-- si no encuentra una coincidencia devuleve 0
print(busqueda_count) #2

#len(variable) <-- Contamos cuantos caracteres tiene una cadena
#len no es un metodo es una función || devuelve el numero de caracteres que tiene una cadena
contar_caracteres = len(cadena_1)# <-- cuenta todos los caracteres, incluido los espacios
print(contar_caracteres)#15

#startswitch() <-- verificamos si una cadena empieza con una cadena dada

empieza_con =  cadena_1.startswith("Hola")# <-- Si es cierto devuelve True, sino devuelve False
print(empieza_con)#True

#endswitch() <-- verificamos si una cadena termina con una cadena dada
termina_con = cadena_1.endswith("Carlos")# <-- Si es cierto devuelve True, sino devuelve False
print(termina_con)#True

#replace() <-- remplaza un pedazo de la cadena dada, por otra dada
#- si no encuentra una coincidencia devuelve la cadena original -
cadena_nueva = cadena_1.replace("Hola","Adios")# <-- replace(parametro_antiguo, parametro_nuevo)
print(cadena_nueva)#Adios soy Carlos

#split() <-- separa la cadena con la cadena que le pasemos
cadena_separada = cadena_1.split(" ")# <-- Devuelve una lista separado por el parametro
print(cadena_separada)#['Hola', 'soy', 'Carlos']
print(cadena_separada[1])#soy

#Estos son metodos principales de los strings o cadenas
#Algunos son funciones como len(variable)
#Usualmente --> metodo() | metodo(parametro) | metodo(parametro_1, parametro_2)
#funciones --> función(variable) <-- se le da la variable como un parametro
