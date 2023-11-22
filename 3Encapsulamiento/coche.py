class Coche:
    def __init__(self,velocidad,km):
        self.velocidad = velocidad
        self._km = km

    @property
    def obtenerKM(self):
        return f"el kilometraje actual es {self._km} km"
    def aumentoKM(self,distancia):
        if distancia > 0:
            self._km += distancia
        return "se aumento el kilometraje"


auto = Coche(200,10)
print(auto.aumentoKM(30))
print(auto.obtenerKM)
auto.self._km = 1