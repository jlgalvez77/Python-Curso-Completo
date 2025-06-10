# Crear un juego de adivinar un número entre 1 y 100
# Con un máximo de 10 intentos.
# Debe mostrar al final si ganó o perdió y mostrar el número secreto al final y el número de intentos
import random

numero_secreto = random.randint(1, 101)
intentos = 0

print('Bienvenido al juego de adivina el número.')
while intentos < 10:
    numero_jugador = int(input('Introduce un número entre 1 y 100.: '))
    intentos += 1
    if numero_jugador <= 0 or numero_jugador >= 100:
        input('Introduce un número entre 1 y 100.')
    elif numero_secreto == numero_jugador:
        print(f'Has acertado que el número era {numero_jugador} en {intentos} intentos.')
        break
    elif numero_secreto > numero_jugador:
        print('Felicidades has ganado.')
        print('Tú número es mas bajo que el número secreto.')
    elif numero_secreto < numero_jugador:
        print('Tú número es mas alto que el número secreto.')
    else:
        print('Itroduce un valor correcto.')
if numero_secreto != numero_jugador and intentos >= 10:
    print(f'Has perdido el número secreto era {numero_secreto}.')