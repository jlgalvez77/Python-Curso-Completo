class Animal:
    """Clase animal, clase de la que heredaran las clases que sean animales"""
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f'Animal: {self.especie}, edad: {self.edad}'

class Mascota(Animal):
    """Clase para representar una mascota, que hereda de la clase Animal"""
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.nombre = nombre

    def __str__(self):
        return f'Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]'

class RegistroMascotas:
    """Clase para representar un registro de mascotas."""
    def __init__(self):
        self.mascotas = []
    """Agrega una mascota al registro de mascotas"""
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        """Lista todas las mascotas registradas"""
        if self.mascotas:
            print('     Lista de mascotas \n')
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f'{i}. {mascota}')
        else:
            print('No hay mascotas registradas')

    def editar_mascota(self, indice, nueva_mascota):
        """Editar una mascota al registro de mascota"""
        if indice < 0 or indice > len(self.mascotas):
            raise ValueError('Mascota indice invalida')
        else:
            self.mascotas[indice] = nueva_mascota
            print('     Mascota editada \n')

    def eliminar_mascota(self, indice):
        if indice < 0 or indice > len(self.mascotas):
            raise ValueError('Mascota indice invalida')
        else:
            del self.mascotas[indice]
            print('     Mascota eliminada \n')