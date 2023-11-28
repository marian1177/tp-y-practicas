import random
n = random.randint(1, 10)


def funcionX():  # bloque de codigo cualquiera que se use para el administrador

    return "codigo particular que realiza algo especifico"


class Notificador():
    def __init__(self, parametro):  # se le pasa un parametro simulando el numero de bloque
        # si se utilizara con archivos, el parametro seria el nombre del archivo
        # sin parametro podria utilizarse el adm contexto sin inicializador
        self.parametro = parametro

    def __enter__(self):  # el msj que se muestra antes de ejectuar el bloque de codigo
        print(f"inicio del bloque del codigo {self.parametro}")
        return self

    def __exit__(self, *args):  # el msj que se muestra despues de ejecutar el bloque de codigo
        print(f"salida del bloque de codigo {self.parametro}")
        return self


with Notificador(n):
    print(funcionX())
