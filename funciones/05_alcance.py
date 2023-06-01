saludo = "1.1 Hola global"  # Alcance global


def saludar():
    saludo = "1. Hola Mundo"  # Alcance de la función
    print(saludo)


def saludaLeonsito():
    saludo = "2. Hola Leonsito"  # Alcance de la función
    print(saludo)


def saludar1():
    global saludo
    saludo = "1.2. Hola Mundo mala practica"

# -> No se imprimirá porque no está al alcance de las variables de las funciones


saludar()
# saludaLeonsito()
resultado1 = saludo + 3
print(resultado1)
saludar1()
resultado2 = saludo + 3
print(resultado2)
