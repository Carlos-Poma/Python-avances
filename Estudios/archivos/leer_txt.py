#usando "open" para abrir un archivo con una codificación 
# universal (UTF-8) a "archivo"
archivo = open("Estudios\\archivos\\texto_de_carlos.txt",encoding="utf-8")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo.readline()

#cerrar el archivo
archivo.close()

print(linea)