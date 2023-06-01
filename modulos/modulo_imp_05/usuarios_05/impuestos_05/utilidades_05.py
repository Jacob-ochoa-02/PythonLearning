if __name__ != "__main__":
    # from ..gestion_05.crud_05 import guardar
    # ".." -> import relativo
    from usuarios_05.gestion_05.crud_05 import guardar
    # import absoluto
    print(__name__)

    def pagar_impuestos():
        print("Pagando impuestos...")
        guardar()

if __name__ == "__main__":
    print("tarea de mantenimiento")
