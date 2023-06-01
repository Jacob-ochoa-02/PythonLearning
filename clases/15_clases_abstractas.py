from abc import ABC, abstractmethod
# Hacer que la clase padre herede de ABC


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):    # Se tiene que definir en la subclase por ser abstracta
        pass            # y ya no se tiene que hacer el constructor

    @abstractmethod
    def guardar(self):  # Indicarnos si se está guardando el dato en la base de datos
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
