class Punto3D:
    def __init__(self, punto_x, punto_y, punto_z):
        self.punto_x = punto_x
        self.punto_y = punto_y
        self.punto_z = punto_z


class Figura3D():  # clase con los metodos abstractos
    pi = 3.14 #dato que sera compartido con las subclases
    def __init__(self, punto_x, punto_y, punto_z):
        self.punto = Punto3D(punto_x, punto_y, punto_z) #pequeña composicion 
    
    def calcular_volumen(self):
        pass

    def calcular_area(self):
        pass


class Cubo(Figura3D):

    def __init__(self, punto_x, punto_y, punto_z):
        super().__init__(punto_x, punto_y, punto_z)

    def calculo_volumen(self):
        # formula de volumen = lado x lado x lado
        return "el volumen del Cubo es :", self.punto.punto_x*self.punto.punto_y*self.punto.punto_z

    def calculo_superficie(self):
        # formula de superficie = superfice de un lado (lado x lado)x 6 caras
        return "la superficie del cubo es: ", self.punto.punto_x**2 * 6


class Esfera(Figura3D):
    

    def calculo_volumen(self):
        # formula de volumen = V = 4/3 π r
        radio = int(
            input("favor de ingresar el radio para calcular la superficie: "))
        return "el volumen de la esfera es :", radio * (4/3*self.pi**3)

    def calculo_superficie(self):
        # formula de superficie = 4 π r 2
        radio = int(
            input("favor de ingresar el radio para calcular la superficie: "))
        return "la superficie del esfera es: ", 4*self.pi*radio*2

class Cilindro(Figura3D):

    def __init__(self, punto_x, punto_y, punto_z):
        super().__init__(punto_x, punto_y, punto_z)

    def calculo_volumen(self):
        # formula de volumen = π r² h
        radio = int(
            input("favor de ingresar el radio para calcular la superficie: "))
        return "el volumen del cilindro es :", self.pi* radio* self.punto.punto_y

    def calculo_superficie(self):
        radio = int(
            input("favor de ingresar el radio para calcular la superficie: "))
        # formula de superficie = 2π r h + 2π r²
        return "la superficie del cilindro es: ", 2*self.pi*self.punto.punto_y+2*self.pi*radio**2 
    

cub = Cubo(3,4,6)
print(cub.calculo_volumen())
print(cub.calculo_superficie())

esf = Esfera(2,0,0)
print(esf.calculo_volumen())
print(esf.calculo_superficie())

cil = Cilindro(0,4,0)
print(cil.calculo_volumen())
print(cil.calculo_superficie())