lista = ['cadena', 'ratón', 'guitar', 'espejo', 'triple',
         'zapato', 'árbol', 'jardín', 'nieve', 'fresco']
print("lista previo a modificacion: ", lista)


def longitud(string): return f"{string}: {len(string) } de longitud"


lista_modificada = map(longitud, lista)

print("lista post modificacion: ", list(lista_modificada))
