# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.

curso_anio = int(input("Ingrese el año del curso: "))

for i in range(3):
    name = input("Ingrese su nombre: ")
    year = int(input("Ingrese su año de nacimiento: "))
    edad = curso_anio - year
    print(f"{name} cumple {edad} años en el {curso_anio}.")

