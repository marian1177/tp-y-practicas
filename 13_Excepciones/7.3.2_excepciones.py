class errordato(Exception):

    print("error no ingreso un dato numerico")


class errorcero(Exception):

    print("error no se divide por cero")


def division(n1, n2):

    if not (isinstance(n1, int) | isinstance(n2, int)):

        raise errordato()
    elif n1 == 0 | n2 == 0:
        raise errorcero()

    else:
        return n1/n2


try:
    n1 = int(input("ingrese n1 "))
    n2 = int(input("ingrese n2 "))
    print(division(n1, n2))
except errordato as e1:
    print(e1)

except errorcero as e2:
    print(e2)

finally:
    print("division finalizada")
