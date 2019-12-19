import math 

base = float(input('base: '))
altura = float(input('altura: '))

hipotenusa = math.sqrt(base**2 + altura**2)

print("la hipotenusa es: {}".format(hipotenusa))