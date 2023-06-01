import usuario


def guardar():
    usuario.guardar()


def guardar(entidad):   # Se le pasa la entidad que requiera la funcion guardar
    entidad.guardar()
    # 1. Permite reutilizar más el codigo
    # 2. Permite desacoplar nuestro codigo para que sea más facil de reutilizar
    # 3. Escribirle el test a nuestro codigo va a ser sumamente sencillo
