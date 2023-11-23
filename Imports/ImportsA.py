#   Crear dos módulos en el mismo directorio. Desde un módulo, importa
#   una función o variable del otro utilizando una importación absoluta.

import random
#   3.1. importacion absoluta 
#from ImportsB import Funcion_ajena_de_datos


#   3.2. esta importacion relativa no me la reconoce el visual, no me reconoce los init como directorios
#   solo utilizando por comando python -m Imports.ImportsA si funciona
#from .ImportsB import Funcion_ajena_de_datos 

#   3.3     3.5.    3.7 tambien solo funciona por comando python -m Imports.ImportsA
#   se le agrega un alias para especificar la ruta a la funcion
#   el llamado quedaria  print (Z.Funcion_ajena_de_datos(r1,r2))
#import Imports.ImportsB as Z 


#   3.4. importacion circular
#from ImportsB import *

#3.6 import con alias
import ImportsB as F
r1=random.randint(1,10)
r2=random.randint(1,10)

def Funcion_de_prueba():

    print ("llamo a la funcion ajena")

    print (F.Funcion_ajena_de_datos(r1,r2))

Funcion_de_prueba()