
def frase(nombre,apellido,adjetivo="Humano"):#Valor predeterminado
    return f'Hola {nombre} {apellido}, eres {adjetivo}'

#Utilizando keywords arguments
frase_resultado = frase(nombre="Carlos", apellido="Poma", adjetivo="Persona")
print(frase_resultado)