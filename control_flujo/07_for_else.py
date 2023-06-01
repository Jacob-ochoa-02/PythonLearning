# Algoritmo de cuando si se encuentra el digito
buscar = 3
for numero in range(5):  # range() es un iterable
    print(numero)
    if numero == buscar:
        print("Encontrado:", buscar)
        break  # con break se detiene la ejecución de la iteración
else:
    print("No encontré el número buscado :c")

# Algoritmo de cuando no se encuentra el digito
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado:", buscar)
        break  # con break se detiene la ejecución de la iteración
else:   # Si no se topa hasta el break, pasa a el for-else
    print("No encontré el número buscado :c")

for char in "Ultimate python":  # Iterar un carácter
    print(char)
