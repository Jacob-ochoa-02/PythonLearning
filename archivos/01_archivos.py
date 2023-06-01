from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()  # Archivo existe
# archivo.rename()  # Renombrar el archivo
# archivo.unlink()  # Eliminar el archivo

# print(archivo.stat())   # Estadisticas del archivo

print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
# timestamp decha con respecto al 1ro de enero de 1970 - fecha unix - Linux o MacOs
