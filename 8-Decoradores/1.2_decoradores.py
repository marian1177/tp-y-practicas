

class Estudiante:
    def __init__(self, nombre, edad, _promedio):
        self.nombre = nombre
        self.edad = edad
        self._promedio = _promedio

    def mostrar_informacion(self):
        return self.nombre, self.edad, self._promedio

    def actualizar_promedio(self, nuevo_promedio: int):
        if nuevo_promedio >= 0:
            self._promedio = nuevo_promedio
            return self._promedio

    def verificador(self):  # verificador de los argumentos de la funcion Promedio
        if not isinstance(self._promedio, int):
            print("Error en tipo de dato")
        else:
            print("Dato OK")

    @verificador
    def promedio(self):
        return self._promedio

    def incrementar_edad(self):

        self.edad += 1
        return self.edad
