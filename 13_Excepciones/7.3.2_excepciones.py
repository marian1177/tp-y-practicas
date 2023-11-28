class errordato(Exception):

    print("error no ingreso un dato numerico")


class errorcero(Exception):

    print("error no se divide por cero")


try:

    opcion = int(input("ingrese el tipo de operacion \n"
                       "1 - suma \n"
                       "2 - resta \n"
                       "3 - division \n"
                       "4 - multiplicación"))

    print("ingrese los numeros a utilizar")
    n1 = int(input("ingrese n1 "))
    n2 = int(input("ingrese n2 "))

    def suma(n1, n2):
        resultado = n1+n2
        return resultado

    def resta(n1, n2):
        resultado = n1-n2
        return resultado

    def division(n1, n2):
        resultado = n1/n2
        return resultado

    def multi(n1, n2):
        resultado = n1*n2
        return resultado

    if opcion == 1:
        print(suma(n1, n2))
    elif opcion == 2:

        print(resta(n1, n2))
    elif opcion == 3:
        if n1 == 0 or n2 == 0:
            raise errorcero("Error no se divide por cero")
        else:
            print(division(n1, n2))
    elif opcion == 4:

        print(multi(n1, n2))
    else:
        raise errordato("error en la opcion ingresada")


except errordato as e1:
    print(e1)

except errorcero as e2:
    print(e2)

finally:
    print("Finished")
