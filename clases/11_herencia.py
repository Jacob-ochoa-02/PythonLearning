class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


perro = Perro()
perro.comer()


class Chanchito(Perro):
    def programar(self):
        print("programando")


chanchito = Chanchito()
chanchito.pasear()
