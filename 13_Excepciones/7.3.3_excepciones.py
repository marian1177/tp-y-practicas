
class errorconarchivo(Exception):
    pass


class archivovacio(Exception):
    pass


try:
    with open("archivoLectura.txt", "r") as archivo:  # leo el archivo
        contenido = archivo.read()  # me guardo el contenido"
    if not archivo:
        raise errorconarchivo("Archivo no existente")
    elif not contenido:
        raise archivovacio("error el archivo esta vacio")

    # abro el otro archivo y escribo el contenido guardado
    with open("archivoEscritura.txt", "w") as archivo2:
        archivo2.write(contenido)

except errorconarchivo as error:
    print(error)
except archivovacio as error2:
    print(error2)


finally:
    print("se cierra archivo")
    archivo.close()
    archivo2.close()
