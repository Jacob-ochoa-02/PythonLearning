from pathlib import Path
import db
import graphql
import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependecias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphql": "esto es graphql"
}


def load(p):
    # -> Se utiliza para importar paquetes y modulos de modo dinámico
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependecias)
    except:
        print("el paquete no tiene funcion init")


list(map(load, paths))
