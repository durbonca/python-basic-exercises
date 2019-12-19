base = float(input('ingrese base: '))
comisiones = 0.0

for i in range(1,4):
    venta = float(input('ingrese venta {}: '.format(i)))
    comision = venta * 10 / 100
    comisiones = comisiones + comision


earning = base + comisiones

print('el total de ganancias del mes son:')
print(earning)