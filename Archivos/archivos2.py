import csv


with open('archivo83.csv', 'r') as archivo:
    lector = csv.DictReader(archivo)
    
    notas =0
    
    for fila in lector:
        
        dato = (fila)
        print (f"{dato}" )
        
archivo.close()

notas = [
    ['Lucas', 'Burki', 7],
    ['Marcos', 'Castelo', 5],
    ['Luis', 'Renna', 4],
    ['Micaela', 'Vidal', 9],
    ['Agustina', 'Ruiz', 3],
    ['Daniel', 'Lopez', 8],
    ['Josefina', 'Gonzalez', 2]
        ]

#with open('archivo83.csv', 'w') as archivo1:
#    escritor = csv.writer(archivo1)
#    for fila in notas:
#        escritor.writerow(fila)
#
#archivo1.close()
