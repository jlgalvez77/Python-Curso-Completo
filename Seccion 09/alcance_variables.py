# Variables Globales
c = 0
c = 10
a = 20

# Función con variables locales
def suma(a, b):
    r = a + b
    print(locals())
suma(3,4)

# Con "global" hacemos que la variable "c" sea global
def ac():
    global c
    c += 1

# Variables no-locales
def func1():
    c = 0   # Variable no-local
    def func2():
        nonlocal c  # Con "nonlocal" convertimos la variable a no-local
        c += 1
    func2()
    print(c)
func1()