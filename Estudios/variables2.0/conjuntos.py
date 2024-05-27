#creando un conjunto con set
conjunto = set(["dato1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 2"}


print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#resultado = conjunto2.issubset(conjunto1)
resultado = conjunto1 > conjunto2

#verificar si hay un número en común
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)