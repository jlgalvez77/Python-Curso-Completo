import random
from typing import List, Dict

def formato_aleatorio() -> str:
    formatos = [
        'Hola, {} Bienvenido',
        'Es genial verte {}',
        'Saludos. {}. Encantado de conocerte'
    ]

    return random.choice(formatos)

def hola(nombre: str) -> str:
    if nombre == '':
        return 'Nombre vacio'

    saludo = formato_aleatorio().format(nombre)
    return saludo

def holas(nombres:List) -> Dict:
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    return saludos