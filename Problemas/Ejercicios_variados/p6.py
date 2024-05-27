#Definir una función es_palindromo() que reconoce palíndromos
#(es decir, palabras que tienen el mismo aspecto escritas invertidas),
#ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    palindromo,palindromo_invertido,i = [],[],0
    for letra in palabra : 
        palindromo_invertido.append(letra)
        palindromo.append(letra)
    palindromo_invertido.reverse()
    while i != len(palabra):
        if palindromo[i] == palindromo_invertido[i]:
            if i + 1 == len(palabra):return True
        i+=1
    return False

resultado = es_palindromo("radar")
print(resultado)

