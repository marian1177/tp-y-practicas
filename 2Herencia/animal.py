class Animal:
    def __init__(self,nombre,edad,raza=None):
        self.nombre = nombre
        self.edad = edad            #atributos que heredaran las subclases
        self.raza =raza

    def desc_raza(self):
        return (f" mi raza es {self.raza}")  #un metodo propio de la clase padre comun a sus subclases
    
class Perro(Animal):
    def __init__(self,nombre,edad,raza):    #herencia directa de atributos, este se usa para mostrar el atributo de la clase padre
        super().__init__(nombre,edad,raza)

class Gato(Animal):
    def __init__(self,nombre,edad,raza,cantidad_bigotes):
        super().__init__(nombre,edad,raza)
        self.cantidad_bigotes = cantidad_bigotes

    def ronronear(self):
        return "el gato esta ronroneando"  #metodo especifico del Gato

class Pajaro(Animal):
    def __init__(self,nombre,edad,color_plumas): #atributos heredados y propios del objeto
        super().__init__(nombre,edad)
        self.color_plumas = color_plumas

cujo = Perro("cujo",1,"ovejero aleman")
print(cujo.desc_raza())
paulie = Pajaro("Paulie",4,"verde")
print(f"Mi nombre es {paulie.nombre}")
