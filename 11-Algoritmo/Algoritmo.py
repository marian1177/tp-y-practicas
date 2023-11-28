import random

numero = random.randint(10000000, 9999999999)


def sumador_pares(numero):

    numstrings = str(numero)  # convierto a string el numero para recorrerlo
    numfinal = 0  # variable para guardar el total
    for i in numstrings:
        print("valor en modo string de i", i)
        if int(i) % 2 == 0:  # convierto a int la variable string y verifico si es multiplo divisible por 2, par
            print("valor de i convertido en int que si es par lo suma", i)
            numfinal = numfinal+int(i)   # se suma si es par
        else:
            print("numero negativo: ", int(i))
            # si es impar le resta 3 a la variable y lo suma
            numfinal = numfinal+int(i)-3
    print("el numero total es ", numfinal)


print("elnumero random sera: ", numero)
sumador_pares(numero)
