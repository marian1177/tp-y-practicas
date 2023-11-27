import threading
import time
# Se importa libr string para utilizar el ascii abecedario
import string       
tiempo = time.time()
#tomo de la funcion time los datos de segundos unicamente
segundos = tiempo % 60
#tomo 2 decimales
segundo = round(segundos,2)
import random

#def contador():
#    for i in range(1,27 ):
#        print (f"[{i} - seg: {segundo}]")
#        #time.sleep(1)


# se recorre el abecedario marcando el segundo ejecutado
def abecedario():
    for i in  string.ascii_lowercase:
        print (f"[{i}  - seg: {segundo}]")
        #time.sleep(1)

n=random.randint(1,10)

    
# se realiza una funcion en paralelo como factorial, se toma de un numero random de una lista
lista_factorial=[]
def factorial(lista_factorial):
    n=random.randint(100000000,999999999)
    for i in range(1,10):
        lista_factorial.append(n)


    resultado=1
    for i in lista_factorial:
        resultado*=i
        print(f"factorial de {i}: {resultado}") 
    print (f"tiempo de ejecucion factorial : {segundo}] segundos")


hilo1 = threading.Thread(target=abecedario)
hilo2 = threading.Thread(target=factorial,args=(lista_factorial,))

hilo1.start()
hilo2.start()

