#si el modulo estuviera dentro de una misma carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar

import sys
sys.path.append('c:\\Users\\carlo\\OneDrive\\Escritorio\\Python-avances\\Estudios\\funciones_buenas')

import saludar as modulo_saludo
print(modulo_saludo.saludar("Carlos"))
