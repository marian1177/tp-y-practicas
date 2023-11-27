with open("archivoLectura2.txt", "r") as archivo2, open("archivoLectura3.txt", "r") as archivo3, open("archivoLectura4.txt", "r") as archivo4:

    contenido2 = archivo2.read()
    contenido3 = archivo3.read()
    contenido4 = archivo4.read()

    with open("archivoEscritura2.txt", "w") as archivoW:
        archivoW.write(f"{contenido2} \n"
                      "---------------------------------------------\n")
        archivoW.write(f"{contenido3} \n"
                       "---------------------------------------------\n")
        archivoW.write(f"{contenido4} \n")


archivo2.close()
archivo3.close()    
archivo4.close()