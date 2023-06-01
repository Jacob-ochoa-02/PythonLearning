# and, or, not
# and es para 2 condiciones que se quieren cumplir
#   ->Si una de ambas no se cumple, entonces lanzará No se cumplirá
# or es para cuando 1 de 2 condiciones se cumplan
#   ->Si ambas no se cumplen, lanzará False
# not es para cuando se requiere negar una operación

gas = True
encendido = True

if gas and encendido:
    # Condición en la que ambas deben cumplirse
    print("1-Puedes avanzar")

gas = False
encendido = True

if gas and encendido:
    # Error para la condición en la que ambas debian cumplirse
    # Pero una de ellas no cumple por ende no entra a la condición
    print("2-Puedes avanzar")

gas = False
encendido = True

if gas or encendido:
    # Condición en la que una de las 2 debe de cumplirse
    print("3-Puedes avanzar")

gas = False
encendido = False

if gas or encendido:
    # Error para la condición en la que una de las 2 debia
    # cumplorse, pero ambas no cumplian
    print("4-Puedes avanzar")

gas = False
encendido = False

if not gas or encendido:
    # Condición en la que una de las 2 debia cumplirse
    # pero con la negación de una y por ende si cumplió con
    # la condición
    print("5-Puedes avanzar")

gas = True
encendido = True
edad = 21

if gas and encendido and edad > 17:
    # Condición en la que las 3 debian cumplirse para
    # Entrar al ciclo
    print("6-Puedes avanzar")

gas = True
encendido = False
edad = 21

if gas and (encendido or edad > 17):
    # Condición en la que ambas debian cumplirse
    # Pero una de ellas incluía 2 variables, en las cuales
    # solo 1na de ellas debia cumplirse
    print("7-Puedes avanzar")


gas = False
encendido = True
edad = 21

if not gas and encendido and edad > 17:
    # Cambiamos la inicialización de una variable para que
    # todas las variables cumplan con la condición a aceptar
    print("8-Puedes avanzar")

gas = False
encendido = False
edad = 16

if not gas or encendido or edad > 17:
    # Cambiamos la inicialización de una variable para que esta
    # variable sea aceptada y esta permita que se cumpla la
    # condición
    print("9-Puedes avanzar")
