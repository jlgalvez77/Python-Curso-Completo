class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f'Animal[Especie: {self.especie} \nEdad: {self.edad}]'

class Mascota(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.__nombre = nombre  # Atributo privado poniendole __ delante

    # Con get podemos accedeer al atributo privado/obtenemos su valor
    def get_nombre(self):
        return self.__nombre

    # Con set podemos modificar el atributo
    def set_nombre(self, nombre):
        self.__nombre = nombre


    def __str__(self):
        return f'Mascota[Especie: {self.especie} \nEdad: {self.edad}, \nNombre: {self.__nombre}]'


mascota = Mascota('Perro', '1 Año', 'Bob')
print(mascota)

mascota.edad = '2 Años'

# print(mascota.__nombre)  Da error al no poder accederse
mascota.set_nombre('Rufus') # Con este metodo podemos cabiar el nombre del atributo protejido
print(mascota.get_nombre()) # Con este metodo podemos imprimir el atributo protejido
print(mascota)