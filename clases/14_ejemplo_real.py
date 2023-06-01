class Model():
    tabla = False

    def __init__(self):  # Verificar definicion de una tabla
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):  # Indicarnos si se está guardando el dato en la base de datos
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(126)  # Buscar por medio de usuario (No deberia)
Usuario.buscar_por_id(123)  # Buscar por medio de la clase de Usuario
