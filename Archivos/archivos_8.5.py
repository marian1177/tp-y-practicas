import csv 
import json 


with open("archivo83.csv", 'r') as A_csv, open("archivoJson", 'w') as archivoJson:
    # Lee los datos del CSV
    datos_csv = csv.DictReader(A_csv)

    # Convierte y escribe los datos en formato JSON
    datos_json = json.dumps(list(A_csv), indent=6) #indent es solo sangria
    archivoJson.write(datos_json)


    # Mostrar el contenido del archivo JSON
    with open("archivoJson", 'r') as archivoJson:
        final = archivoJson.read()
        print("datos", datos_json)