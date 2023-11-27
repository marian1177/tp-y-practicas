


with open("archivoLectura.txt", "r") as archivo1:
   
    contenido = archivo1.read()
    with open("archivoEscritura.txt", "w") as archivo2:
        archivo2.write(contenido)

archivo1.close()
archivo2.close()
