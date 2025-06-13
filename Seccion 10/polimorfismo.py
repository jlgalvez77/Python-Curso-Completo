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

    def hablar(self):
        pass

    def __str__(self):
        return f'Mascota[Especie: {self.especie} \nEdad: {self.edad}, \nNombre: {self.nombre}]'

mascota = Mascota('Perro', '2 Años', 'Bob')
print(mascota)

class Perro(Mascota):
    def hablar(self):
        return 'Woof!'

class Gato(Mascota):
    def hablar(self):
        return 'Miauu!'

p = Perro('Perro', '1 Año', 'Bob')
g = Gato('Gato', '6 Meses', 'Pelusa')

print(p.hablar())
print(g.hablar())