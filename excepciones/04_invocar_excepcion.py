def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por 0", f"{n}")
        # 1. No deberias lanzar excepciones muy seguido por ser
        # costosas en rendimiento, osea, si puedes pero si los errores
        # son explicitos
        # 2. Tú puedes crear tus propias excepciones personalizadas
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
