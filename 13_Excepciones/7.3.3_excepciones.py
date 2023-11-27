
class errorconarchivo(Exception):
    pass


try:
    with open("archivoLectura.txt", "r") as archivo: #leo el archivo
        contenido = archivo.read() #me guardo el contenido"

    with open("archivoEscritura.txt", "w") as archivo2: #abro el otro archivo y escribo el contenido guardado
        archivo2.write(contenido)
    
except errorconarchivo as error:
    print(error)

else:
    print("Se leyó el archivo y se escribió en otro.")

finally:
    print("se cierra archivo")
    archivo.close()
    archivo2.close()
    