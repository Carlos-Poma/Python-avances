
#crear una funcion que verifique si es primo
def es_primo(num):
    #verifica que si el número que le pasamos es primo
    for i in range(2,num-1):
        if num%i == 0: return False #retorna si no es primo
    return True #retorna si es primo

def primos_hasta(num):
    lista_num_primos = []
    #encontramos todos los números primos hasta el número dado
    for i in range(3, num + 1): #omitimos el 2 
        #Colocamos la función para comprobar que sea primo
        if es_primo(i): lista_num_primos.append(i) #añadimos a la lista los números primos
    return lista_num_primos



#Llamamos a la función para hallar todos los números primos
resultado = primos_hasta(100)
#Mostramos la liste de números primos
print(resultado)