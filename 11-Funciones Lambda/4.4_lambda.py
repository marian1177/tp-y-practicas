import math
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("lista previo a modificacion: ", lista)


funcion_raiz = lambda n: round(math.sqrt(n),2)


lista_modificada = map(funcion_raiz, lista)

print("lista post modificacion:     ", list(lista_modificada))