mi_dicc = {}

print(type(mi_dicc))

datos_personales = {'nombre': 'Jose',
                    'edad': 48,
                    'ciudad': 'Gijón'
                    }
print(datos_personales['nombre'])

print('nombre' in datos_personales)
print(datos_personales.get('profesión', 'No especificada'))
print(datos_personales.get('nombre', 'No especificada'))

datos_personales['clave1'] = 'Valor1'
print(datos_personales)
datos_personales['clave1'] = 'Valor1'
print(datos_personales)
datos_personales.update({'clave2': 'Valor2'})
print(datos_personales)
datos_personales.update({'clave2': 'valor2'})
print(datos_personales)
datos_personales.update({'clave3': 'Valor3', 'clave4': 'Valor4'})
print(datos_personales)
del datos_personales['clave3']
print(datos_personales)
datos_personales.pop('clave4')
print(datos_personales)
print(len(datos_personales))
print(datos_personales.keys())
print(datos_personales.values())
print(datos_personales.items())