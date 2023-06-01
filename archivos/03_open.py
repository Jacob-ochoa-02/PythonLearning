from io import open

# escritura
# texto = "Hola mundo!"

# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with y seek
# with se encarga de cerrar nuestro archivo sin tener que indicarselo
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())  # Carga todo el archivo en memoria
#     archivo.seek(0)  # Ve a un caracter en especifico
#     for linea in archivo:   # Cara solo de a una linea a la vez
#         print(linea)
# __enter__ -> se ejecuta cuando hayamos abierto el archivo
# __exit__ -> se ejecuta cuando se haya ejecutado todo lo del bloque with
# se está cerrando el archivo de manera automatica

# agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("Chao mundo :(")
# archivo.close()

# lectura y escritura
with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz la"
    archivo.writelines(texto)
    # Lee todas las lineas dentro del archivo, agregadas agregarlas como una lista
    # y moverá el puntero hasta el final
