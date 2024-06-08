#Definir una función generar_n_caracteres()
#que tome un entero n y devuelva el caracter multiplicado por n. 
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"

generar_n_caracteres = lambda entero,n:entero*n

multiplucacion = generar_n_caracteres(5,"x")
print(multiplucacion)