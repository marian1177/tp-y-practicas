class Producto:  # clase basica del producto con los datos basicos
    def __init__(self, nombre, precio, stock, tipo):
        self.nombre = nombre
        self.tipo = precio
        self.stock = stock
        self.tipo = tipo
        # una lista que guardara los datos , se separan para utilizar gondola con indice
        self.gondola = [nombre, precio, stock, tipo]

    def mostrar_producto(self):
        return ("el producto seleccionado es {self.nombre} del sector {self.tipo}")

    def mostrar_totales(self):
        # por medio de indice se muestran los datos
        return f"producto: {self.gondola[0]}, precio {self.gondola[1]}, stock: {self.gondola[2]}"


class Carrito(Producto):  # clase que trayendo los datos de la clase Producto los ira guardando en un 'carrito'

    def __init__(self):
        # self.producto = Producto(self.nombre)
        self._totales_prod = []

    def agregar_producto(self, producto):
        self._totales_prod.append(self.producto.nombre)
        # se guarda solo el nombre del producto para poder contarlos

        # se puede eliminar productos
    def eliminar_producto(self):
        self._totales_prod.remove(self.producto.nombre)

    @property  # se protege los totales
    def producto(self):
        return self._totales_prod

    # con un length se verifica el largo de la lista seran los productos
    def mostrar_totales(self):
        totales = len(self._totales_prod)
        return f"hasta ahora hay {totales} de productos"


class Cliente:  # clase de clientes para datos de acceso al servicio
    def __init__(self, nombre, clave, nivel_acceso):
        self.nombre = nombre
        self._clave = clave
        self.nivel_acceso = nivel_acceso  # se protegela clave

    @property
    def verificar_clave(self):
        return self._clave

    def seteo_de_clave(self, nueva_clave):
        # se puede modificar la clave si es distinta a la anterior y tiene mas de 8 caracteres
        if nueva_clave != self._clave and len(self._clave) > 8:
            self._clave = nueva_clave

    def modificar_producto(self):
        # metodo que segun el tipo de acceso podria modificar algun producto, pasada a administrador
        pass

    def datos_cliente(self):
        return f"cliente: {self.nombre} tiene nivel de acceso {self.nivel_acceso}"


class Pedido:
    pass


class Administrador(Cliente):
    def __init__(self, nombre, clave, nivel_acceso, control):
        super().__init__(nombre, clave, nivel_acceso)
        self.control = control

     # se heredan datos y se implementa el metodo de modificar productos segun el acceso
    def modificar_producto(self, nuevo_nombre, nuevo_stock):
        if self.nivel_acceso == 1:
            Producto.nombre = nuevo_nombre
            Producto.stock = nuevo_stock

        return ("el producto a cambiar es el {self.producto.nombre}")


# instancia de prueba, se carga una breve lista de productos
productos = [
    Producto("Pan Lactal", 890.74, 10, "Almacen"),
    Producto("Mermelada", 1024, 5, "Almacen"),
    Producto("Patitas Pollo", 4050, 3, "Congelados"),
    Producto("Seven UP", 1200, 14, "Bebidas")
]
for producto in productos:
    print(producto.mostrar_totales())


carrito_de_cliente = Carrito()
carrito_de_cliente.agregar_producto("Seven UP")

print(carrito_de_cliente.mostrar_totales())
