"""
Crea una clase llamada "Estudiante" con los siguientes atributos: nombre, edad y _promedio.
Implementa tres métodos: mostrar_informacion() para mostrar los detalles del estudiante,
actualizar_promedio(nuevo_promedio) para cambiar el promedio del estudiante y
incrementar_edad() para aumentar en 1 la edad del estudiante cada vez que se llama.
Además, crea una propiedad llamada promedio para acceder y modificar el promedio de
manera controlada.
"""
class Estudiante:
    def __init__(self, nombre, edad, _promedio):
        self.nombre = nombre
        self.edad = edad
        self._promedio = _promedio

    def mostrar_informacion(self):
        return self.nombre, self.edad, self._promedio
    
    def actualizar_promedio(self, nuevo_promedio:int):
        if nuevo_promedio >= 0:
            self._promedio = nuevo_promedio
            return self._promedio
        
    @property
    def promedio(self):
        return self._promedio
    
    
    def incrementar_edad(self):

        self.edad += 1
        return self.edad     
    
nom = str(input("Ingrese el nombre del estudiante: \n" ))
edad = int(input("A continuación la edad del estudiante: \n"))
prome = int(input("A continuacion ingrese el promedio del estudiante: \n"))
alumno = Estudiante(nom,edad,prome)
print(f"Los datos ingresados son: \n" 
      f"Alumno: {alumno.nombre} \n"
      f"Edad: {alumno.edad}\n"
      f"Promedio: {alumno._promedio}")

prome = int(input("Actualice el nuevo promedio del estudiante...:\n"))
print(f"El nuevo promedio es:  {alumno.actualizar_promedio(prome)}\n")
(alumno.incrementar_edad())

print(f" Datos con el promedio actualizado: {alumno.mostrar_informacion()}")