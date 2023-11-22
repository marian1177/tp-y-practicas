class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self._calificaciones = []

    
    @property
    def calificaciones(self):
        return f"las notas guardadas son: {self._calificaciones}"
    
    def agregar_calificacion(self,nota):
        
        nuevanota = nota
        if isinstance(nota, (int)) and 0 < nota <= 10:
            self._calificaciones.append(nuevanota)
        else:
            return "usted ingreso una nota erronea"


alumno = Estudiante("mariano",35)
alumno.agregar_calificacion(7)
print(alumno.calificaciones)
alumno.agregar_calificacion(9)
print(alumno.calificaciones)
print(alumno.agregar_calificacion("fsdf"))
print(alumno._calificaciones(10))    
