
class errordivision(ValueError):
    pass


class errorindices(ValueError):
    pass


class errorstrintoint(ValueError):
    pass


class errorarchivo(FileNotFoundError):
    pass


class errorclave(KeyError):
    pass


def division(n1, n2):

    if n2 == 0:
        raise errordivision("error en digito 2 es cero")

    else:
        return n1/n2


try:
    division(3, 6)
except errordivision:
    print(errordivision)

n1 = int(input("ingrese n1"))
n2 = int(input("ingrese n2"))

print(division(n1, n2))


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
busqueda = int(input("ingrese la posicion de indice para acceder al dato"))
try:

    print("el dato en el indice indicado es: ", lista[busqueda])
    if busqueda > len(lista) or busqueda < 0:
        raise errorindices("Error indice fuera de rango")

except errorindices:

    print(errorindices)


try:
    cadena = str(input("Ingrese una cadena que represente un número: "))
    print("La cadena ingresada fue:", cadena)

    if cadena.isdigit():
        numero = int(cadena)
        print("El número es:", numero)
    else:
        raise errorstrintoint(
            "Error, la cadena no representa un número válido.")


except errorstrintoint:
    print(errorstrintoint)


try:
    archivo = open("archivo.txt", "r")
    if not archivo:
        raise errorarchivo("Archivo no existente")

except errorarchivo:
    print(errorarchivo)


dic = {
    "alumnoA": "luis",

    "alumnoB": "tomi",

    "alumnoC": "lucas",

}


print(dic)


try:
    print(dic['alumnoa'])
    if not dic['alumno']:
        raise errorclave("clave erronea")

except errorclave:
    print(errorclave)
