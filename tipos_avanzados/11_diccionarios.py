# Izquierda string, Derecha cualquier cosa [Izquierda:Derecha]
punto = {"x": 25, "y": 50}
# print(punto)
# print(punto["x"])
# print(punto["y"])

punto["z"] = 45  # ->Ingresar un ndato en el diccionario
# punto["lala"] = 20
# print(punto, punto["lala"])
if "lala" in punto:
    print("Encontré lala", punto["lala"])

print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])
print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "Nombre": "Leonsito"},
    {"id": 2, "Nombre": "Feliz"},
    {"id": 3, "Nombre": "Jacob"},
    {"id": 4, "Nombre": "Gambito"},
]

for usuario in usuarios:
    print(usuario["Nombre"])
