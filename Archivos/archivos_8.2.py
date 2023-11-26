class errorconarchivo(Exception):
    pass


try:
    with open("archivoLectura.txt", "r") as archivo:  # leo el archivo
        # print ("Se abre archivo")
        contenido = archivo.read()

    # Variable que almacena el total y un contador que se setea en Cero cuando NO hay
    # letras que conformen una palabra.
    cantidad_palabras = 0
    contador = 0

    for caracter in contenido:
        # Si hay un espacio, salto o tabulacion se usa el boolean para decir que NO 
        # estamos dentro de una palabra.
        if caracter == ' ' or caracter == '\n' or caracter == '\t':
            in_palabra = False
            # print (" ",end=" " )
            if contador > 0:
                # Si el contador estuvo acumulando lectura y estamos en un espacio
                # se suma cantidad de palabras y se reinicia el contador.
                cantidad_palabras = cantidad_palabras+1
            contador = 0
        else:
            in_palabra = True
         #   print (caracter,end=" ")
            contador = contador+1


except errorconarchivo as error:
    print(error)


finally:
    # print("se cierra archivo")
    print("cantidad de palabras en el archivo de txt: ", cantidad_palabras)
    archivo.close()
