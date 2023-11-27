import threading
import time
# Se importa lib string para utilizar el ascii abecedario
import string       
tiempo = time.time()
#tomo de la funcion time los datos de segundos unicamente
segundos = tiempo % 60
#tomo 2 decimales
segundo = round(segundos,2)
import random
import queue

cola_compartida = queue.Queue(maxsize=5)
productos =['pan lactal', 'leche', 'azucar', 'seven up', 'yerba']
def cliente():
    

    for producto in productos:
        producto = random.choice(productos)
        cola_compartida.put(producto)

        print (f"se saca del carrito para escanear el producto {producto}")

        #espera de unos segundos para dar otro producto a escanear
        time.sleep(random.randint(1,2))

# el cajero recibe los productos a destiempo
def cajero():
    for producto in productos:
        producto = cola_compartida.get()
        print(f"BEEEP! {producto} escaneado")
        time.sleep(random.randint(2,5))

        
    

hilo1 = threading.Thread(target=cliente)
hilo2 = threading.Thread(target=cajero)

hilo1.start()
hilo2.start()

