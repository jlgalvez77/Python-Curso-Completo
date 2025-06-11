# Indicamos que a la variable "a" le asignamos un entero
a: int = 400
# Indicamos que va a recibir un entero "a" y un entero "b", e informamos que la función devuelve un entero
def suma(a: int, b: int) -> int:
    return a + b

def saludo(nombre: str, veces:int) -> str:
    return f'{nombre}' * veces
print(saludo(nombre = 'Jose', veces = 5))