texto = 'hola mundo'

print(texto.title())    # Pone en mayusculas la primera letra de cada palabra
print(texto.upper())    # Pone en mayusculas todas las letras
print(texto.lower())    # Pone en minusculas todas las letras
print(texto.count('o')) # Cuenta cuantas veces aparece la letra en el texto
print(texto.find('h'))  # Muestra el indice de la primera coincidencia
print(texto.index('h')) # Muestra el indice de la letra

texto = 'Python'
nuevo_texto = texto.replace('P', 'S')   # Reemplaza una letra por otra
print(nuevo_texto)

texto = 'Hola mundo de Python'
print('Hola' in texto)  # Nos dice si existe la cadena en la cadena