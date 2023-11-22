class Coche:
    def __init__(self,velocidad,km):
        self.velocidad = velocidad
        self._km = km  #atributo protegido a utilizar

    @property
    def obtenerKM(self):        #se devuelve el dato protegido unicamente llamandolo por el metodo
        return f"el kilometraje actual es {self._km} km"
    def aumentoKM(self,distancia):   #metodo de modificacion del atributo 
        if distancia > 0:
            self._km += distancia
        return "se aumento el kilometraje"


auto = Coche(200,10)
print(auto.aumentoKM(30))
print(auto.obtenerKM)
auto.self._km = 1  #forzado de error