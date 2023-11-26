lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("lista previo a modificacion: ", lista)


funcion_multi = lambda n: n * 2


lista_modificada = map(funcion_multi, lista)

print("lista post modificacion:     ", list(lista_modificada))
