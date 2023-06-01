class Ave:  # Clase Padre
    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("vuela ave")


class Pato(Ave):    # Sub clase
    def __init__(self):
        super().__init__()
        self.nada = "nadador"

    def vuela(self):
        print("vuela pato")
        super().vuela()  # Acceso inmediato a todos los metodos de la clase padre


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
