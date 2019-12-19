""" Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra. """
total = 0

base = int(input('ingrese cantidad de productos: '))


for i in range(1,base+1):
    venta = float(input('ingrese valor del producto {}: '.format(i)))
    total = total + venta

descuento = venta * 15 / 100    

print('el total del descuento es:')
print(descuento)