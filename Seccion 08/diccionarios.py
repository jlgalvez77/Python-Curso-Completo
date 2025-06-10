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