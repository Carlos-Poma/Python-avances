
frutas = ["banana","manzana","ciruela","pera","durazno"]
cadena = "Hola Carlos"
numeros = [2,5,8,9,10,23]

#evitando que se coma una manzana
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f'Voy a comer una {fruta}')
    
#Evitar que el bucle se siga ejecutando(el else no se ejecuta)
for fruta in frutas:
    print(f'Voy a comer una {fruta}')
    if fruta == "pera":
        break
else:
    print("terminado")
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)