diccionario = {
    "nombre":"Carlos",
    "apellido":"Poma",
    "subs":10000000
}
#keys() <-- Nos devuele un objeto dict_item
claves = diccionario.keys()
print(claves)

#get() <-- Obteniendo un elemento y si no encuentra nada el programa continua
claves_2 = diccionario.get("nombre")
print(claves_2)#Carlos

#pop() <-- Elimina un elemento del diccionario
diccionario.pop("subs")

#items() <-- Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
#dict_items([('nombre', 'Carlos'), ('apellido', 'Poma')])





#clear() <-- Elimina todos los elementos del diccionario