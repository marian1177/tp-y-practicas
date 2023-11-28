


try:
    archivo = open("archivo.txt", "r")
    if not archivo:
        raise FileNotFoundError("Archivo no existente")

except FileNotFoundError:
    print(FileNotFoundError)