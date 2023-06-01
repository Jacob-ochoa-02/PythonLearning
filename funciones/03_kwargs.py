def get_product(**datos):
    # Con Key Words Arguments se deben usar 2 asteriscos = "**"
    # lo que imprime se llama -> Diccionario
    print(datos["id"], datos["name"])


# Si se llama con 2 asteriscos a una funcion que tiene como parametro
# 2 asteriscos = **, deberemos poner el nombre del parametro que queremos
# que sea asignado en la función cuando hagamos referencia a él
get_product(id="26", name="Hola", desc="Esto es un ejemplo")
