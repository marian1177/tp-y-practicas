class Coche:
    def __init__(self,velocidad,km):
        self.velocidad = velocidad
        #atributo protegido a utilizar
        self._km = km  

    @property
    #se devuelve el dato protegido unicamente llamandolo por el metodo
    def obtenerKM(self):        
        return f"el kilometraje actual es {self._km} km"
    #metodo de modificacion del atributo 
    def aumentoKM(self,distancia):   
        if distancia > 0:
            self._km += distancia
        return "se aumento el kilometraje"


auto = Coche(200,10)
print(auto.aumentoKM(30))
print(auto.obtenerKM)
#forzado de error
auto.self._km = 1  