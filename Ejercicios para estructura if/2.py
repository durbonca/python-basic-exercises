""" Ejercicio 2
Algoritmo que pida un número y diga si es positivo, negativo o 0. """

numero = float(input('ingrese valor: '))

if numero > 0:
    print('el numero es positivo')
elif 0 > numero:
    print('el numero es negativo')
else:
    print('el numero es igual a cero')