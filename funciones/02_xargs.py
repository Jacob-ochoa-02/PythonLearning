def suma(*numeros):
    # * Esta instruccion vuelve a este parámetro en una variable
    # Iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 6)
suma(2, 8, 7, 58)
