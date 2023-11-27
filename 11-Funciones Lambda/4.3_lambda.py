lista = ['cadena', 'ratón', 'guitar', 'espejo', 'triple',
         'zapato', 'árbol', 'jardín', 'nieve', 'fresco']
print("lista previo a modificacion: ", lista)


def funcion_mayus(n): return len(n)


lista_modificada = map(funcion_mayus, lista)

print("lista post modificacion: ", list(lista_modificada))
