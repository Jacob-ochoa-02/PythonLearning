bienvenida = f"""
Bienvenidos a la calculadora :D

Las operaciones son:
1. Suma
2. Resta
3. Multiplicacion
4. Division
Escribe "salir" para poder salir

"""
print(bienvenida)
resultado = ""
while True:
    if not resultado:
        resultado = input("Ingresa un número: ")
        if resultado.lower() == "salir":
            print("Gracias por usar la calculadora")
            break
        resultado = int(resultado)
    operacion = input("Ingresa la operación deseada: ")
    if operacion.lower() == "salir":
        print("Gracias por usar la calculadora")
        break
    n2 = input("Ingresa el 2do número: ")
    if n2.lower() == "salir":
        print("Gracias por usar la calculadora")
        break
    n2 = int(n2)
    if operacion == "1":
        resultado += n2
    elif operacion == "2":
        resultado -= n2
    elif operacion == "3":
        resultado *= n2
    elif operacion == "4":
        resultado /= n2
    else:
        print("Operación no válida :c")
        break
    print(f"El resultado es {resultado}")
