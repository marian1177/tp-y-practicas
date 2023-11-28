
class errorconarchivo(Exception):
    pass


try:
    archivo = open("archivoLectura.txt", "r")
    print(archivo.read())
    if not archivo:
        raise FileNotFoundError("no existe el archivo")

except FileNotFoundError:
    print(FileNotFoundError)

finally:
    print("se cierra archivo")
    archivo.close()
