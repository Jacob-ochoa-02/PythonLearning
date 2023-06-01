# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes
# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string
# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y vevolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)]
# 4. de un listado de tuplas, devolver las
# que tengan el mayor valor.
# [("a", 3), ("b", 2), ("c", 4)] -> [("c"), 5]
# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten con 4
from pprint import pprint

# Primer ejercicio

string = "Hola mundo este es mi string"


def primero(texto):
    return [char for char in texto if char != " "]

# Segundo ejercicio


def contar_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

# Tercer ejercicio


def ordenamiento(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )

# Cuarto ejercicio


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

# Quinto ejercicio


def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacios = primero(string)
contados = contar_caracteres(sin_espacios)
ordenados = ordenamiento(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
# contar()
