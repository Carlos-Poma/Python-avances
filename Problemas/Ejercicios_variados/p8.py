#Definir una función generar_n_caracteres()
#que tome un entero n y devuelva el caracter multiplicado por n. 
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"

def generar_n_caracteres(entero,n):
    caracteres = ""
    for num in range(entero):caracteres+=n
    return caracteres

multiplucacion = generar_n_caracteres(5,"x")
print(multiplucacion)