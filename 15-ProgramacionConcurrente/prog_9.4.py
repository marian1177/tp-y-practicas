#Se importan las librerias correspondientes a utilizar
from multiprocessing import Pool
import time
from datetime import datetime

#se captura y formatea la hora actual a utilizar como dato de inicio y fin del proceso
fecha_actual = datetime.now()
hora_actual = fecha_actual.timestamp()
hora_actual_formateada = datetime.fromtimestamp(hora_actual)
solohora = hora_actual_formateada.strftime("%H:%M:%S")

#funcion que tomara el pool de proceso
def calculo(n):
    return 2*n


lista = [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    print("Lista a procesarse: ", lista)
    comienzo = time.time()
    print("Proceso comienza a las: ", datetime.fromtimestamp(comienzo).strftime("%H:%M:%S"))
    #se le indica al pool con cuantos procesadores se trabaja (irrelevante en pruebas basicas de consumo de memoria baja)
    with Pool(3) as p:
        print("Los resultados del uso de la funcion sobre la lista son: ",
              p.map(calculo, lista))

    fin = time.time()
    print("Proceso termina a las: ",
          datetime.fromtimestamp(fin).strftime("%H:%M:%S"))
    tiempo_total_ejecucion = round((fin-comienzo), 4)

    print(f"Tiempo de ejecución total: {tiempo_total_ejecucion} segundos")
