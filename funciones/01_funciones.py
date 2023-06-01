def hola(nombre, apellido="Albino"):
    # En la función se llaman Parámetros las variables
    # Que se emplean en la función
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Jacob", "Ochoa")
# Cuando llamamos a la función se llaman
# Argumentos que le daremos a la función
hola("Leon")

hola(apellido="Ochoa", nombre="Jacob")
# Si trocamos las varuables, deberemos definirlas en el
# argumento para que este pueda ser usado en el orden deseado
