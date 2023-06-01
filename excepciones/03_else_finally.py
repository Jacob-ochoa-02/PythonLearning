try:
    n1 = int(input("Ingresa primer número: ").strip())
except ValueError as e:
    print("Ocurrio un error!")
else:
    print("No ocurrió ningún error :D")
finally:
    print("Se ejecuta siempre!")
