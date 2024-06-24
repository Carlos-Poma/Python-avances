#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
def mas_larga(lista):
    mayor = 0
    for cadena in lista:
        contador = len(cadena)
        if contador > mayor:
            mayor = contador
            cadena_mayor = cadena
    return cadena_mayor

lista_de_texto = ["adios","chau","carlos","pol"]
print(mas_larga(lista_de_texto))
