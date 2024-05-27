
# #Creando una función simple
# def saludar():
#     print("Hola ¿como estas?")

# #ejecutando una función simple
# saludar()

#Crear una función con parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "Femenino"
    elif sexo == "hombre":
        adjetivo = "Masculino"
    else:
        adjetivo = "Otro"
        
    print(f'Hola {nombre} ¿Como estas? {adjetivo}')


saludar("Carlos","cactus")
saludar("Carlos","Mujer")
saludar("Carlos","HoMbre")


#crear una función que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num -5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    return contraseña,num


#Desempaquetando la función
password, primer_numero = crear_contraseña_random(981)


#Mostrando los resultados obtenidos y los datos utilizados
frase = f'Tu nueva contraseña es: {password}'
print(frase)
print(f'El número utilizado para crearlo fue {primer_numero}')