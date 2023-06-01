from usuario_01 import guardar, pagar_impuestos
# 1na forma de importar
# |->recomendada
# No usar un * para un import, ya que es una pesima practica
guardar()  # -> es un modo, (mejor practica) con el import de la 1ra linea


def guardar():      # Pésima práctica, pero es otro modo
    print("soy app.py")
