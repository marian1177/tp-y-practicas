


try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("El archivo no existe")
else:

    archivo.read()
    print("se lee el archivo")
    archivo.close()