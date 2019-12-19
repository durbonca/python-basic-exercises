""" Ejercicio 1

Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no. """

a = float(input('ingrese primer valor: '))
b = float(input('ingrese segundo valor: '))

if a > b:
    print('a es mayor que b')
elif b > a:
    print('b es mayor que a')
else:
    print('a es igual que b')