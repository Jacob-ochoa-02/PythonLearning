numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)
# No se puede modificar una tupla, pero si se puede extraer sus datos
# a otra lista y modificar el dato EN la lista
listaNumeros = list(numeros)
listaNumeros[0] = "Leonsito Feliz"
print(listaNumeros)
