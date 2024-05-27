#creando diccionario con dict()
diccionario = dict(nombre = "Carlos", apellido = "Poma")

#las listas no pueden ser claves y usamos frozenset parqa meter conjuntos
diccionario = {("dalto","rancio"):"jajas"}

#creando un diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"])





print(diccionario)