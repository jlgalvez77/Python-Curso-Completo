from saludos import hola, holas

print(hola('Jose'))

nombres = ['Jose', 'Andrea', 'Pedro', 'Carlos']
saludos = holas(nombres)

for saludo in saludos.values():
    print(saludo)