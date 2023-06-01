class Usuario():
    def guardar(self):
        print("guardando en BBDD")


class Sesion():    # Le permite al servidor cuando un usuario se está conectando
    def guardar(self):
        print("guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])
