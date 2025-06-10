regitro_estudiantes = []

while True:
    print('''Bienvenido al sistema de registros de estudiantes
    1. Registrar Estudiante
    2. Mostrar Registro
    3. Salir''')

    opcion = input('Introduce una opcion: ')

    if opcion == '1':
        nombre = input('Introduce el nombre: ')
        edad = int(input('Introduce el edad: '))
        curso = input('Introduce la curso: ')

        estudiante = {'Nombre': nombre, 'Edad': edad, 'Curso': curso}
        regitro_estudiantes.append(estudiante)
        print('Estudiante registrado correctamente\n')

    elif opcion == '2':
        if regitro_estudiantes:
            print('\nRegistro de Estudiantes:')
            for estudiante in regitro_estudiantes:
                print(f'Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}, Curso: {estudiante["Curso"]}')
        else:
            print('El registro de estudiantes está vacio')

    elif opcion == '3':
        print('Saliendo...')
        break
    else:
        print('Opcion no valida')