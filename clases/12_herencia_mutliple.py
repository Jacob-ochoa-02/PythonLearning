class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Perro:
    def pasear(self):
        print("paseando al perro")

# Derecha a izquierda pero se reemplazan los de la derecha
# con los de la izquierda, si es que tiene un método igual


class Chanchito(Perro):
    def programar(self):
        print("programando")


chanchito = Chanchito()
chanchito.pasear()
