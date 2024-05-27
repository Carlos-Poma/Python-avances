otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5



#Diferencias de duración
diferencia_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_min = round(diferencia_min, 2)
diferencia_max = 100 - dalto_curso / otros_cursos_max * 100
diferencia_max = round(diferencia_max, 2)
diferencia_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
diferencia_promedio = round(diferencia_promedio, 2)

#Calculando el porcentaje de tiempo de promedio vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_promedio = round(tiempo_vacio_promedio, 2)
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto /10
tiempo_vacio_dalto = round(tiempo_vacio_dalto, 2)




#Mostrando las diferencias de duración
print("-----------------------------------")
print(f'El curso de Dalto dura un {diferencia_min}% menos que el más rapido')
print(f'El curso de Dalto dura un {diferencia_max}% menos que el más lento')
print(f'El curso de Dalto dura un {diferencia_promedio}% menos que el promedio')
print("-----------------------------------")

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso eliminó el {tiempo_vacio_dalto}% de tiempo vacio')
print("-----------------------------------")

#Mostrando diferentes diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de este curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de otros cursos')
print("-----------------------------------")

