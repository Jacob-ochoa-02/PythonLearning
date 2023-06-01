import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)
print(
    random.random(),    # crear numeros aleatorios
    # Desde donde hasta donde crear los numeros aleatorios
    random.randint(1, 10),
    lista,  # Desordenar listas
    random.choice(lista2),  # un elemento aleatorio de una lista
    # más de un elemento aleatorio de una lista
    random.choices(lista2, k=3),
    "".join(random.choices("abcdefghi.,123", k=3))  # aplicable a strings
)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
print(seleccion)

contrasena = "".join(seleccion)
print(contrasena)
