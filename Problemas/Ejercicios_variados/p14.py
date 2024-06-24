#Construir un pequeño programa que convierta números binarios en enteros.

# 00101011 ---------  2**n  ------- -1 -> 1

def binario_a_entero(codigo):
    entero,i,n = 0,1,0
    while n < len(codigo):
        if int(codigo[-i]) == 1 : entero +=2**n
        i+=1
        n+=1
    return entero
binario = input("ingrese un codigo binario") # 01101101
print(binario_a_entero(binario))