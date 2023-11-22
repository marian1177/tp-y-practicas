import random
class Persona:
    
    def __init__(self,nombre=str,edad=int,altura=int):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura 

    def mostrar_informacion(self):
      return Persona
      
    def incrementar_edad(self,rand):
       self.edad += rand  
       return self.edad
    
    def cambiar_altura(self,alt):
       self.altura = alt
       return self.altura
    

atleta = Persona("mariano",35,177)

print(f"el nombre del atleta cargado es: {atleta.nombre}\n"
      f"la edad cargada es: {atleta.edad}\n" 
      f"La altura cargada es: {atleta.altura}"
      )

rand=random.randint(1,3)
print(f"Han pasado {rand} años, asi que el atleta ahora tiene {atleta.incrementar_edad(rand)}")
alt = random.choice([x for x in range(161,197) if x != 177])
print(f"La altura del atleta era incorrecta, se corrige a {atleta.cambiar_altura(alt)} cm")
