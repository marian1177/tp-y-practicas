
class FigurasGeometricas():

    #metodos declarados sin implementar
    def calc_area(self):
        pass                    
    def calc_per(self):
        pass
    
    def mostrar_datos(self):
        pass


class Circulo(FigurasGeometricas):

    def __init__(self,radio):       
        self.radio = radio

    # se implementan los metodos
    def calc_area(self):
        return 3.14*self.radio**2           
    
    def calc_per(self):
        return self.radio*2*3.14
    
    def mostrar_datos(self):
        return "el radio del circulo es {self.radio}"
    

class cuadrado(FigurasGeometricas):
    def __init__(self,lado):
        self.lado = lado

    # se sobreescribe metodo
    def mostrar_datos(self):                
        return "el lado del cuadrado es {self.lado}"
    

class Triangulo(FigurasGeometricas):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def mostrar_datos(self):
        return "la base y altura del triangulo son: {self.base} y {self.altura}"