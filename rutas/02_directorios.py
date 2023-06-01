from pathlib import Path

path = Path("rutas")
# path.exists()
# path.mkdir()    # -> Make director, crear carpeta o directorio
# path.rmdir()    # -> Remove director, eliminar carpeta o
# # directorio pero tiene que estar vacio
# path.rename("chanchito-feliz") # -> Cambia el nombre del directorio
# for p in path.iterdir():
#     print(p)
# archivos = [p for p in path.iterdir() if not p.is_dir()]
# archivos = [p for p in path.glob("01_*.py")]
# Todos los .py dentro de todas las carpetas dentro de mi paquete
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
