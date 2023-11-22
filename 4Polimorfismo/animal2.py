class Animal:
    def __init__(self,nombre,edad,raza=None):
        self.nombre = nombre
        self.edad = edad
        self.raza =raza

    def desc_raza(self):
        return (f" mi raza es {self.raza}")
    def hablar(self):
        pass
    
class Perro(Animal):
    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad,raza)
    def hablar(self):
        return "Perro esta ladrando"


class Gato(Animal):
    def __init__(self,nombre,edad,raza,cantidad_bigotes):
        super().__init__(nombre,edad,raza)
        self.cantidad_bigotes = cantidad_bigotes

    def ronronear(self):
        return "el gato esta ronroneando"

    def hablar(self):
        return "Gato esta maullando"

class Pajaro(Animal):
    def __init__(self,nombre,edad,color_plumas):
        super().__init__(nombre,edad)
        self.color_plumas = color_plumas

    def hablar(self):
        return "Pajara esta silbando"

cujo = Perro("cujo",1,"ovejero aleman")
print(cujo.desc_raza())
print(cujo.hablar())

paulie = Pajaro("Paulie",4,"verde")
print(f"Mi nombre es {paulie.nombre}")
print(paulie.hablar())