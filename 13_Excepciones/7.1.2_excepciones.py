import random


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
busqueda = int(input("ingrese la posicion de indice para acceder al dato"))
try:

    print("el dato en el indice indicado es: ", lista[busqueda])
    if busqueda > len(lista) or busqueda < 0:
        raise ValueError("Error indice fuera de rango")

except ValueError:

    print(ValueError)
