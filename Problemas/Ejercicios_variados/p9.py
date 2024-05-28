# Definir un histograma procedimiento()
#que tome una lista de números enteros e imprima un histograma en la pantalla.
#Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******
def generar_n_caracteres(entero,n):
    caracteres = ""
    for num in range(entero):caracteres+=n
    return caracteres

def procedimiento(lista):
    for elemento in lista :
      histograma = generar_n_caracteres(elemento,"*")
      print(histograma)

procedimiento([4,9,7])