# Definir un histograma procedimiento()
#que tome una lista de números enteros e imprima un histograma en la pantalla.
#Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******
generar_n_caracteres = lambda entero,n: entero*n
def procedimiento(lista):
    for elemento in lista :
      histograma = generar_n_caracteres(elemento,"*")
      print(histograma)

procedimiento([4,9,7])