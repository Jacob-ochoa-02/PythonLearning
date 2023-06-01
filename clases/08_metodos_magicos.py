class Perro:
    # __init__ es el constructor
    # Los metodos mágicos son aquellos métodos que se ejecutarán
    # cuando no los llamemos directamente
    def __init__(self, nombre, edad):  # <- Este por ejemplo es un método mágico
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro 😔 {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Leonsito", 7)
# print(perro)
# texto = str(perro)
# print(texto)
del perro
