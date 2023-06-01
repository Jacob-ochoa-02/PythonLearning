animal = "  chanCHito feliz  "
print(animal.upper())  # Se ponen todas las letras del string en Mayúscula
print(animal.lower())  # Se ponen todas las letras del string en minúscula
print(animal.strip().capitalize())
# Se cortan los espacios que se tengan a la izquierda y a la derecha del string (.strip())
# Hace que el primer caracter del string esté en Mayúscula (.capitalize())
print(animal.title())
# Se ponen las primeros caracteres de cada palabra del stringen Mayúscula
print(animal.lstrip())  # Se cortan los espacios del lado izquierdo del string
print(animal.rstrip())  # Se cortan los espacios del lado derecho del string
print(animal.find("cH"))
# Se busca la cadena de caracteres en el string pero sale con -1
print(animal.find("ch"))
# Se busca la cadena de caracteres en el string y muestra el indice de dónde se encuentra
# Reemplazamos la cadena de caracteres deseada por otra
print(animal.replace("nCH", "j"))
print("fe" in animal)
# Se busca si esta cadena de caracteres se encuentra en el string, devuelve true Si está
# devuelve false si no se encuentra en el string
print("fe" not in animal)
print(animal.strip())
# El not hace que veamos si NO se encuentra la cadena de caracteres en el string string
