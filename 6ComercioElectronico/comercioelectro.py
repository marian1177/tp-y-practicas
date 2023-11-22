class Producto:
    def __init__(self, nombre, precio, stock, tipo):
        self.nombre = nombre
        self.tipo = precio
        self.stock = stock
        self.tipo = tipo
        self.gondola = [nombre, precio, stock, tipo]

    def mostrar_producto(self):
        return ("el producto seleccionado es {self.nombre} del sector {self.tipo}")

    def mostrar_totales(self):

        return f"producto: {self.gondola[0]}, precio {self.gondola[1]}, stock: {self.gondola[2]}"


class Carrito(Producto):

    def __init__(self):
        #self.producto = Producto(self.nombre)
        self._totales_prod = []

    def agregar_producto(self,producto):
        self._totales_prod.append(self.producto)
        #self.stock = -cant

    def eliminar_producto(self):
        self._totales_prod.remove(self.producto.nombre)

    @property
    def producto(self):
        return self._totales_prod

    def mostrar_totales(self):
        totales = len(self._totales_prod)
        return f"hasta ahora hay {totales} de productos"

class Cliente:
    def __init__(self, nombre, clave, nivel_acceso):
        self.nombre = nombre
        self._clave = clave
        self.nivel_acceso = nivel_acceso

    @property
    def verificar_clave(self):
        return self._clave

    def seteo_de_clave(self, nueva_clave):
        if nueva_clave != self._clave and len(self._clave) > 8:
            self._clave = nueva_clave

    def modificar_producto(self):
        pass

    def datos_cliente(self):
        return f"cliente: {self.nombre} tiene nivel de acceso {self.nivel_acceso}"


class Pedido:
    pass


class Administrador(Cliente):
    def __init__(self, nombre, clave, nivel_acceso, control):
        super().__init__(nombre, clave, nivel_acceso)
        self.control = control

    def modificar_producto(self, nuevo_nombre, nuevo_stock):
        if self.nivel_acceso == 1:
            Producto.nombre = nuevo_nombre
            Producto.stock = nuevo_stock

        return ("el producto a cambiar es el {self.producto.nombre}")


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