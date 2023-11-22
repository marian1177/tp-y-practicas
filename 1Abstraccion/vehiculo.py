class Vehiculo:

    def __init__(self,marca,modelo,veloz_max):
        #se protegen los atributos porque seran propiedades
        self._marca = marca
        self._modelo = modelo
        self._veloz_max = veloz_max

    @property #propiedades comunes de vehiculo
    def mostrar_basico(self):
            return self._marca, self._modelo, self._veloz_max
    #a modo de simplificar no se aplica metodo de modifcacion
    

class Coche(Vehiculo):
    
        def __init__(self,marca,modelo,veloz_max,puertas,ventanas):
            super().__init__(marca,modelo,veloz_max) # se hereda a findes de funcion de print
            self.puertas = puertas
            self.ventanas =ventanas  #abstraccion atributos especificos de cada objeto

        def despliega_techo(self):    #abstraccion, metodo declarado no implementado
            pass
         

class Moto(Vehiculo):
    def __init__(self,marca,modelo,veloz_max,caja_asiento):
         super().__init__(marca,modelo,veloz_max)
         self.caja_asiento=caja_asiento

    def hacer_willy(self):
         return ("la parte frontera de la moto se eleva haciendo willy")

class Bici(Vehiculo):
    def __init__(self,marca,modelo,veloz_max,pedales):
        super().__init__(marca,modelo,veloz_max)
        self.pedales = pedales

    def hacer_willy(self):
         return ("la parte frontera de la bici se eleva haciendo willy")

#instancia creacion del auto
porche = Coche("Porche 512","Sport",350,2,4) #instancia del auto

#mostrar los datos basicos del auto todo junto por tupla
datos_del_auto = [porche.mostrar_basico]
print("los datos basicos del auto son: ",datos_del_auto )

#mostrar los datos separados
marca = porche._marca 
print("la marca del auto es: ",marca)