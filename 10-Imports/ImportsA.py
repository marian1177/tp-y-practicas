
#   3.1. importacion absoluta:
#from ImportsB import *


#   3.2. 
#Llamo de forma relativa a la clase ClaseModuloB del modulo ImportsB.
#La clase VaciaA pudiendo acceder al modulo ImportsB hace un print de lo que devuelva la funcion del B:
#from Imports.ImportsB import ClaseModuloB
# class VaciaA:
#   print (ClaseModuloB.funcion_ModuloB())


#   3.3     3.5.    3.6
#import ImportsB as Z 
#print(Z.ClaseModuloB.funcion_ModuloB())


#3.4. importacion circular:
#from ImportsB import *

#3.6 import  relativo con alias:
#from Imports.ImportsB import ClaseModuloB as Z
#class VaciaA:
# print (Z.funcion_ModuloB())