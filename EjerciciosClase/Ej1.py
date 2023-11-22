class Producto:
    def __init__(self,nombre,tipo,stock):
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock

    def mostrar_producto(self):
        return ("el producto seleccionado es {self.nombre} del sector {self.tipo}")

class Carrito:
    def __init__(self):
        self.producto = Producto(nombre=str,tipo=str,stock=int)
        self.totales_prod=[]
    def agregar_producto(self):
        self.totales_prod.append(self.producto)

class Usuario:
    def __init__(self,nombre,clave,nivel_acceso):
        self.nombre = nombre
        self._clave =clave
        self.nivel_acceso = nivel_acceso

    @property
    def verificar_clave(self):
        return self._clave

    def seteo_de_clave(self,nueva_clave):
        if nueva_clave != self._clave and self._clave.length > 8:
            self._clave = nueva_clave

    def modificar_producto(self):
        pass

class Pedido:
    pass

class Cliente(Usuario):
    def __init__(self,nombre,clave,nivel_acceso,cupones):
        super().__init__(nombre,clave,nivel_acceso)
        self.cupones=cupones


class Administrador(Usuario):
    def __init__(self, nombre, clave, nivel_acceso,control):
        super().__init__(nombre,clave,nivel_acceso)
        self.control=control
    
    def modificar_producto(self):
        return ("el producto a cambiar es el {self.producto.nombre}")