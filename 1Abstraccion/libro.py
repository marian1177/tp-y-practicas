
class Libro:
    def __init__(self,titulo,autor,precio):
        self.titulo = titulo
        self.autor = autor          #atributos base a cargar los datos de libro
        self.precio = precio



class Libreria:

    def __init__(self):
        self.lista = []         #se guarda en una lista los libros

    def agregar_libros(self,Libro):
        self.lista.append(Libro)        #llamado el metodo se agregan los nuevos datos, libro(clase)

    def calc_precio_total(self):
        precio_total = 0
        for libro in self.lista:            #se recorre la lista de los libros solo para extraer el precio y despues sumarlo
            precio_total += libro.precio

        return precio_total

#instancia
libro1 = Libro("señor de los anillos","JRRT",200)
libro2 = Libro("el silencio de los inocentes","Michael Roldan",500)


libreria= Libreria()
libreria.agregar_libros(libro1)
libreria.agregar_libros(libro2)

print("Lista de libros en la librería:")
for libro in libreria.lista:
    print(f"{libro.titulo} - {libro.autor} - ${libro.precio}")

precio_total_libros = libreria.calc_precio_total()
print(f"\nPrecio total de los libros en la librería: ${precio_total_libros}")





