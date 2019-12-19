""" 
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.

30% de la calificación del examen final.

15% de la calificación de un trabajo final. 

"""
total_parciales = 0.0

for i in range(1,4):
    parcial = float(input('ingrese nota parcial {}: '.format(i)))
    total_parciales = total_parciales + parcial

examen_final = float(input('ingrese nota examen final: '))

trabajo_final = float(input('ingrese nota trabajo final: '))

promedio_parciales = total_parciales / 3

promedio_parciales = promedio_parciales * 55 / 100
examen_final = examen_final * 30 / 100
trabajo_final = trabajo_final * 15 / 100

print ('parciales{},examen{},trabajo{}'.format(promedio_parciales,examen_final,trabajo_final))

nota_final = trabajo_final + examen_final + promedio_parciales  

print('su nota final es: {}'.format(nota_final))