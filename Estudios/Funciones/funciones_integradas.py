numeros = [4,7,1,42,15]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.3456543, 2)
print(numero)

#retorna False -> 0, vacio, False,  \ True -> distinto a 0, True, cadena, datos no vacios
resultado = bool(-1)#True

#retorna True, si todos los valores son verdadero
resultado_all = all([234,"True",[23,344]])#True


#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)