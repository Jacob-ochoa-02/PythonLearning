from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")


class Sesion(Model):    # Le permite al servidor saber cuando un usuario se está conectando
    def guardar(self):
        print("guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
# Entregar a la funcion guardar 2 objetos que cumplen con una
# interfaz necesaria para ser ejecutada por nuestra funcion
guardar([sesion, usuario])  # |->Polimorfismo
# Polimorfismo es para llamar una función de cada uno de los objetos sin necesidad
# de llamar el metodo de guardar varias
