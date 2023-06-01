class Coordenadas:
    def __init__(self, lat, lon):
        # lat = latitud
        # lon = longitud
        self.lat = lat
        self.lon = lon

    # con eq infiere instantaneamente cuál va a ser el método ne
    # Metodo mágico
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    # Metodo not equal -> ne

    # def __ne__(self, otro):
    #     return self.lat != otro.lat or self.lon != otro.lon

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


# 0x000002223141E710 -> Dónde se encuentra guardada fisicamente en la memoria ram
# esta instancia de la clase
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords != coords2)
print(coords >= coords2)
