from pathlib import Path

# Path(r"C:\Archivos de Programa\Minecraft")
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()  # Si es un archivo
path.is_dir()   # Si es un directorio o carpeta
path.exists()   # Si existe

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

# -> Permite cambiarle el nombre al archivo
p = path.with_name("chanchito.exe")
print(p)
# -> Permite cambiarle el sufijo o extension al archivo
p = path.with_suffix(".bat")
print(p)
# -> Permite cambiarle el nombre al archivo pero sin su extension
p = path.with_stem("feliz")
print(p)
