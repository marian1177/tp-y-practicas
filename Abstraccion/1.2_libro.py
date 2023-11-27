
class Libro:
    def __init__(self, titulo, autor, precio):
        # atributos base a cargar los datos de libro
        self.titulo = titulo
        self.autor = autor
        self.precio = precio


class Libreria:

    def __init__(self):
        # se guarda en una lista los libros
        self.lista = []

    def agregar_libros(self, Libro):
     # llamado el metodo se agregan los nuevos datos, libro(clase)
        self.lista.append(Libro)

    def calc_precio_total(self):
        precio_total = 0
      # se recorre la lista de los libros solo para extraer el precio y despues sumarlo
        for libro in self.lista:
            precio_total += libro.precio

        return precio_total


# instancia
libro1 = Libro("señor de los anillos", "JRRT", 200)
libro2 = Libro("el silencio de los inocentes", "Michael Roldan", 500)


libreria = Libreria()
libreria.agregar_libros(libro1)
libreria.agregar_libros(libro2)

print("Lista de libros en la librería:")
for libro in libreria.lista:
    print(f"{libro.titulo} - {libro.autor} - ${libro.precio}")

precio_total_libros = libreria.calc_precio_total()
print(f"\nPrecio total de los libros en la librería: ${precio_total_libros}")
