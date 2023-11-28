

def invertir_cadena(cadena):  # funcion que se llama asi misma hasta agotar caracteres
    if len(cadena) == 0:  # limite cuando recorta los ultimos caracteres y queda la cadena vacia
        return cadena
    else:  # devuelve el utlimo caracter de la cadena
        # se toma todos los caracteres de la cadena menos el ultimo
        return cadena[-1] + invertir_cadena(cadena[:-1])


cadena = "mariano"
print(invertir_cadena(cadena))
