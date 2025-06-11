# Argumentos indefinidos
def args_fun(*args):
    print(args)

args_fun(1, 2, 3, True, 45.5, 'Python')

# Argumentos posicionales
def suma(a, b):
    print(f'a = {a}, b = {b}')
    return a + b
print(suma(b = 3, a = 4))

def kwargs_fun(**kwargs):
    print(kwargs)
kwargs_fun(a = 1, b = 2, c = 3)
# Se pueden mezclar los argumentos que se passan
def argumentos(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

argumentos(500, 'Hola', True, 400, nombre = 'Jose', b = 500)
