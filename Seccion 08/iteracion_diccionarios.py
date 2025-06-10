datos = {'nombre':'Jose', 'edad':48, 'ciudad': 'Gijon'}

for valor in datos:
    print(valor)

for valor in datos:
    print(datos[valor])

for valor in datos.values():
    print(valor)

for valor in datos.keys():
    print(valor)

for clave, valor in datos.items():
    print(clave, valor)