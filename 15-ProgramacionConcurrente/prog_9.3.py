import multiprocessing
import queue
import random
import threading
import time
tiempo = time.time()
# tomo de la funcion time los datos de segundos unicamente
segundos = tiempo % 60
# tomo 2 decimales
segundo = round(segundos, 2)


cola_compartida = queue.Queue(maxsize=5)
productos = ['pan lactal', 'leche', 'azucar', 'seven up', 'yerba']


def cliente():

    for producto in productos:
        producto = random.choice(productos)
        cola_compartida.put(producto)

        print(f"se saca del carrito para escanear el producto {producto}")

        # espera de unos segundos para dar otro producto a escanear
        time.sleep(1)


# el cajero recibe los productos a destiempo
def cajero():
    for producto in productos:
        producto = cola_compartida.get()
        print(f"BEEEP! {producto} escaneado")
        time.sleep(0.1)


if __name__ == '__main__':
    proc_cliente = multiprocessing.Process(target=cliente)
    proc_cajero = multiprocessing.Process(target=cajero)

    time.sleep(10)
    proc_cliente.start()
    breakpoint
    proc_cajero.start()

    proc_cliente.join()
    proc_cajero.join()
