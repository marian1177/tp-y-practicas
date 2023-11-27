class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        # se guardan las calificaciones en una lista
        self._calificaciones = []  

    
    @property    
    #dato sensible protegido solo traido por el metodo       
    def calificaciones(self):
        return f"las notas guardadas son: {self._calificaciones}"
    
    def agregar_calificacion(self,nota):    
        #validacion para agregar datos a la lista
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
#forzado de error
print(alumno.agregar_calificacion("fsdf"))  
print(alumno._calificaciones(10))    
