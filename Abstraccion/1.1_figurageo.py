import random       #se importa un random para generacion de datos numericos
class FigurasGeometricas(): 

    def calc_area(self):
        pass                #metodos abstractos que seran utilizados en las subclases
    def calc_per(self):
        pass

class Circulo(FigurasGeometricas):

    def __init__(self,radio): 
        
        self.radio = radio          #atributo especifico de circulo

    def calc_area(self):
        return 3.14*self.radio**2      #implementacion de los metodos declarados
    
    def calc_per(self):
        return self.radio*2*3.14


class Rectangulo(FigurasGeometricas):

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura        
    
    def calc_area(self):
        return self.base*self.altura
    
    def calc_per(self):
        return self.base*2+self.altura*2
    
class Triangulo(FigurasGeometricas):

    def __init__(self,base,altura):
        self.altura = altura
        self.base = base

    def calc_area(self):
        return (self.altura*self.base)/2  
    
    def calc_per(self):
        return self.base*3


rand=random.randint(1,9)
circulo= Circulo(rand)
rectangulo= Rectangulo(rand,rand)
triangulo= Triangulo(rand,rand)

print (f"El area de un circulo de radio {rand} es: {circulo.calc_area()}")
print (f"El perimetro de un circulo de radio {rand} es: {circulo.calc_per()}")

print (f"El area de un Rectangulo de base {rand} y altura {rand} es: {rectangulo.calc_area()}")
print (f"El perimetro de un Rectangulo de base {rand} y altura {rand} es: {rectangulo.calc_per()}")

print (f"El area de un Triangulo de base {rand} y altura {rand} es: {triangulo.calc_area()}")
print (f"El perimetro de un Triangulo de base {rand} es: {triangulo.calc_per()}")
