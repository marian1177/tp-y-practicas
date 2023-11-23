import time
import random
def retardo(sub):
    n= random.randint(1,4)
    print (f"se realiza un retraso de {n} segundos")
    time.sleep(n)
    return sub

@retardo
def funcion_interna(n1,n2):

    resultado = n1 + n2
    
    return "suma luego del retardo: ", resultado

n1 =3
n2 =5
print(funcion_interna(n1,n2))
