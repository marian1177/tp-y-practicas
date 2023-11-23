
class errorconarchivo(Exception):
    pass

try:
    archivo = open("archivoLectura.txt", "r")
except errorconarchivo as error:
    print(error)
else:

    archivo.read()
    print("se lee el archivo")

finally:
    print("se cierra archivo")
    archivo.close()
