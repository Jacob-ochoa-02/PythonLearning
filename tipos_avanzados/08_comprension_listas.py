usuarios = [
    ["Leonsito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:  # Forma coloquial
#     nombres.append(usuario[0])
# print(nombres)
# Forma más elegante
# Transformar - map
# nombres = [usuario[0] for usuario in usuarios]
# Filtrar - filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# nombres = [usuario[0]
#    for usuario in usuarios if usuario[1] > 2]  # Filtra y transforma-map and filter
# Usando funcion Map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
# Usando funcion filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
