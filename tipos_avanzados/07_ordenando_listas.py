numeros = [2, 3, 48, 56, 68, 20]

# numeros.sort(reverse=True) # Me altera la lista
# numeros2 = sorted(numeros)  # No la altera para un uso futuro
# las ordena en orden Ascendente
numeros2 = sorted(numeros, reverse=True)
# las ordena en orden Descendente
print(numeros)
print(numeros2)

usuarios = [
    ["Leonsito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# parm -> parametro
# lambda parametro: valor de retorno
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
