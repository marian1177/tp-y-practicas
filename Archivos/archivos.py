class errorconarchivo(Exception):
    pass


try:
    with open("archivoLectura.txt", "r") as archivo: #leo el archivo
        contenido = archivo.read()

    # Contador de palabras encontradas
    cantidad_palabras = 0

    for caracter in contenido:
        # si hay espacio , saltos o tabulaciones cuenta como contenido
        if caracter == ' ' or caracter == '\n' or caracter == '\t':
            in_palabra = False
        elif cantidad_palabras == 0:
         #si encuentra al menos 1
            in_palabra = True
            cantidad_palabras =cantidad_palabras + 1
    

except errorconarchivo as error:
    print(error)


finally:
    print("se cierra archivo")
    print("cantidad de palabras: ", cantidad_palabras)
    archivo.close()
