import random


list=[]

for i in range(1,10):

    n=random.randint(1,10)
    list.append(n)
print(list)

busqueda = int(input("ingrese la posicion de indice para acceder al dato"))
if busqueda > len(list) or busqueda < 0:
    raise ValueError("numero fuera del rango de indices")
else:
    print(f"el indice elegido trae el dato: ",list[busqueda])    

try:
    print(list[busqueda])
except ValueError:
    print(ValueError)
