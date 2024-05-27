#Definir una función es_palindromo() que reconoce palíndromos
#(es decir, palabras que tienen el mismo aspecto escritas invertidas),
#ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    lista_invertida = []
    lista_palabra = []
    for letra in palabra:lista_invertida.append(letra)
    
    lista_palabra = lista_invertida.reverse()
    longitud = len(palabra)
    for rango in range(0,longitud):
        if lista_palabra[rango] != lista_invertida[rango]: return False
    return lista_palabra
    
print(es_palindromo("hola"))
