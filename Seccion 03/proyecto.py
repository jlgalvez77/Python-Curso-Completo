print('*** Calculo de Precio de Venta ***')

impuesto = 0.18

precio_compra = float(input('Ingresa el precio de compra: '))
precio_venta = (precio_compra * impuesto) + precio_compra

print(f'El precio de venta es: {precio_venta}')
