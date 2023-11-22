class Forma:
    def __init__(self, color, dimension1, dimension2=None):
        self.color = color
        self.dimension1 = dimension1
        self.dimension2 = dimension2

    def calc_area(self):
        pass

    def calc_perim(self):
        pass


class Circulo(Forma):

    PI = 3.14

    def __init__(self, color, dimension1):
        super().__init__(color, dimension1)
        self.radio = dimension1

    def calc_area(self):
        return f"el circulo de color {self.color} tiene un area de: {self.PI * self.radio**2}"

    def calc_perim(self):
        return f"el circulo de color {self.color} tiene un perimetro de  {self.PI * 2 * self.radio}"


class Rectangulo(Forma):
    def __init__(self, color, dimension1, dimension2):
        super().__init__(color, dimension1, dimension2)
        self.base = dimension1
        self.altura = dimension2

    def calc_area(self):
        return f"el circulo de color {self.color} tiene un area de: {self.base * self.altura}"

    def calc_perim(self):
        return f"el circulo de color {self.color} tiene un perimetro de  {self.base*2+self.altura*2}"


cir = Circulo("verde", 7)
print(cir.calc_area())
print(cir.calc_perim())
