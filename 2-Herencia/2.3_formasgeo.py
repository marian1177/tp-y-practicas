class Forma:
    def __init__(self, color, dimension1, dimension2=None):
        # Se le deja none a dimension 2 en caso  de no usarla. por eso queda ultima posicion
        self.color = color
        self.dimension1 = dimension1
        self.dimension2 = dimension2

    # metodo a implementar por las subclases
    def calc_area(self):
        pass

    def calc_perim(self):
        pass


class Circulo(Forma):

    # atributo de clase compartido
    PI = 3.14  

    def __init__(self, color, dimension1):
        super().__init__(color, dimension1)
        # atributo heredado
        self.radio = dimension1  

    def calc_area(self):  
        # se aplica la fomula directa del calc de area de un circulo
        return f"el circulo de color {self.color} tiene un area de: {self.PI * self.radio**2}"

    def calc_perim(self):  
        # se aplica la fomula directa del calc de perimetro de un circulo
        return f"el circulo de color {self.color} tiene un perimetro de  {self.PI * 2 * self.radio}"


class Rectangulo(Forma):
    def __init__(self, color, dimension1, dimension2):
        # objeto que SI utiliza las 2 dimensiones
        super().__init__(color, dimension1, dimension2)
        self.base = dimension1
        self.altura = dimension2

    def calc_area(self):
        return f"el circulo de color {self.color} tiene un area de: {self.base * self.altura}"

    def calc_perim(self):
        return f"el circulo de color {self.color} tiene un perimetro de  {self.base*2+self.altura*2}"


# instancia de prueba
cir = Circulo("verde", 7)
print(cir.calc_area())
print(cir.calc_perim())
