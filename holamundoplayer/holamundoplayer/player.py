"""
Este es el modulo que incluye la clase
de reproductor de musica
"""


class Player:
    """
    Esta clase crea un reproductor 
    de musica
    """

    def play(self, song):
        """
        Reproduce la canción que recibio como parámetro

        Parameters:
        song (str): este es un string con el path de la cancion

        Return:
        int: devuelve 1 si reproduce con exito, devuelve 0 en caso de fracaso
        """
        print("reproduciendo canción")

    def stop(self, song):
        """
        Detiene la cancion que recibió como parámetro

        Parameters:
        song (str): este es un string con el path de la canción

        Return:
        int: devuelve 1 si detiene con exito, devuelve 0 en caso de fracaso
        """
        print("stopping")
