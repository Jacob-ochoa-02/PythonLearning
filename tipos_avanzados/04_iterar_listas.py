mascotas = ["Pelusa", "Pulga", "Felipe", "Leonsito Feliz"]

# enumerate() -> enumera instantaneamente los elementos de la lista
# y los inserta en una "tupla"
# (0, 'nombre')
# 0 = indice, nombre = nombre de la variable
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
