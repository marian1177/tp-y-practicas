# Libreria para utilizar la funcion Didctreader
import csv


with open('archivo83.csv', 'r') as archivo:
    # se utiliza el DictReader para leer los datos del CSV
    lector = csv.DictReader(archivo, delimiter='\t')

    notas = 0
    Promedio = 0
    cantidad_de_notas = 0
    acumulado = 0
    min = 10
    max = 0

    for fila in lector:
        # Se leen los datos de la columna Nota del archivo para calcular promedio, max y min
        if 'Nota' in fila and fila['Nota'].strip():
            # Convierte el valor de la nota a entero
            nota = int(fila['Nota'].strip())
            # print(nota)
            cantidad_de_notas += 1
            acumulado += nota

            if nota > max:
                max = nota
            #    print("el maximo actual hasta ahora es:", max)
            elif nota < min:
                min = nota
            #    print("el minimo actual hasta ahora es: ", min)

        # Se realiza un filtro sobre los apellidos, buscando la primer letra y verificando si se encuentra
        # de la mitad del abecedario hasta el final
        if ' apellido' in fila and fila[' apellido'].strip():
            apellidos = fila[' apellido'].strip()
            # print("Apellido es: ",apellidos)
            ape_lista = [apellidos]
            for apellido in ape_lista:
                primeraletra = apellido[0]
                if 'N' <= primeraletra <= 'Z':
                    print(
                        f"El alumno: {apellido} rendira examen en la segunda fecha")

        else:
            print("error de recooleccion de info: ", fila)
    # print ("la cantidad de notas son: ",cantidad_de_notas)
    # print("la suma total de las notas es: ",acumulado)
    Promedio = acumulado/cantidad_de_notas
    print("El promedio de notas es: ", round((Promedio), 2))
    print("La menor nota es: ", min)
    print("El maximo de nota es: ", max)


archivo.close()

# notas =
# [
# ['Lucas',	 'Burki',	    7],
# ['Marcos',	 'Castelo',	5],
# ['Luis',	 'Renna',	    4],
# ['Jose',	 'Guitirrez',	9],
# ['Micaela',	 'Bianchi',	9],
# ['Daniel',	 'Lopez',	    8],
# ['Damian',	 'Materi',    9]
# ]


# with open('archivo83.csv', 'w') as archivo1:
#    escritor = csv.writer(archivo1)
#    for fila in notas:
#        escritor.writerow(fila)
#
# archivo1.close()
