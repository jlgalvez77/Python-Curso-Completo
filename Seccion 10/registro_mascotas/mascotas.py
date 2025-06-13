class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f'Animal[Especie: {self.especie} \nEdad: {self.edad}]'

animal1 = Animal('Perro', '1 Año')
animal2 = Animal('Gato', '6 Meses')

class Mascota(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.nombre = nombre
    def info(self):
        print(f'Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}')

    def __str__(self):
        return f'Mascota[Especie: {self.especie} \nEdad: {self.edad}, \nNombre: {self.nombre}]'

mascota = Mascota('Perro', '2 Años', 'Bob')
mascota.info()
print(mascota)