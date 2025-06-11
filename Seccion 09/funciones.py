def saludar(nombre):
    print(f'Hola {nombre} desde la función saludar.')

saludar('Jose')

def saludar1(nombre):
    return f'Hola {nombre}!'

saludo = saludar1('Jose')
print(saludo)

def suma(a, b):
    return a + b
print(suma(3,4))