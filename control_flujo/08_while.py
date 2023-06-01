# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

# comando = ""

# while comando.lower() != "salir":
# Se usa para que ejecute una función hasta que el
# Usuario desee salir
#     comando = input("$ ")
#     print(comando)

# comando = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break   
    # otra forma de cerrar el ciclo para que no consuma memoria demás
