mascotas = ["Pelusa", "Wolfgang", "Pulga",
            "Felipe", "Wolfgang", "Leonsito Feliz"]

mascotas.insert(4, "Aurora")  # Insertar
mascotas.append("Leonsito triste")  # Agregar al final

mascotas.remove("Wolfgang")
# Eliminar el primer elemento que encuentre
mascotas.pop(1)
del mascotas[1]
mascotas.clear()  # Limpia la lista entera
print(mascotas)
