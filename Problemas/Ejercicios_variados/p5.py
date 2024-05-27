#Definir una función inversa() que calcule la inversión de una cadena.
#Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
def inversa(caracteres):
    caracteres_invertido = []
    texto = ""
    for caracter in caracteres:caracteres_invertido.append(caracter)
    caracteres_invertido.reverse()
    for invertido in caracteres_invertido:texto = texto + invertido
    return texto


print(inversa("estoy probando"))
        