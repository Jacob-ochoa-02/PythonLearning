class Perro:
    def habla(self):    # Primer parametro siempre será self
        print("Guau!")


mi_perro = Perro()
# print(type(mi_perro)) # Ver el tipo de variable
mi_perro.habla()
print(isinstance(mi_perro, Perro))
