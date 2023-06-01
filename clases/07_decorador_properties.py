class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    # Sirve para indicar que convierta el metodo en una propiedad
    @property   # Solo para getters
    def nombre(self):
        print("pasando por getter")
        return self.__nombre

    @nombre.setter  # Así le indicaremos que esté será el setter
    def nombre(self, nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Leonsito")
print(perro.nombre)
