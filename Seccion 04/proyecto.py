# Comprobar si una palabra es palindromo
palabra = input('Introduce una palabra: ').lower().replace(' ','')

palabra_alreves = palabra[::-1]

if palabra == palabra_alreves:
    print(f'La palabra {palabra} es palindromo')
else:
    print(f'La palabra {palabra} no es palindromo')