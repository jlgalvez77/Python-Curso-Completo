from proyecto import Mascota, RegistroMascotas

registro = RegistroMascotas()

while True:
    menu = """--- Menú ---
    1. Agregar mascota
    2. Listar mascotas
    3. Editar mascota
    4. Eliminar mascota
    5. Salir
    Introduce una opción: """

    opcion = int(input(menu))
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        especie = input("Ingrese el especie: ")
        edad = input("Ingrese la edad: ")

        mascota = Mascota(especie, edad, nombre)
        registro.agregar_mascota(mascota)

    elif opcion == 2:
        registro.listar_mascotas()

    elif opcion == 3:
        indice = int(input("Ingrese el indice: "))
        nombre = input("Ingrese el nombre: ")
        especie = input("Ingrese el especie: ")
        edad = input("Ingrese la edad: ")

        nueva_mascota = Mascota(especie, edad, nombre)
        registro.editar_mascota(indice-1 ,nueva_mascota)

    elif opcion == 4:
        indice = int(input("Ingrese el indice: "))
        registro.eliminar_mascota(indice-1)

    elif opcion == 5:
        print("Saliendo")
        break

    else:
        print("Opcion no valida")