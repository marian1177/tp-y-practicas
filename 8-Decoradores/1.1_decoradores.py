cont = 0    #acumulado de veces llamada la funcion

def funcion_a(funcion_b):
    def funcion_c(a, b):
        global cont #global le indica que la variable es la externa para pasar el dato
        cont += 1  # Incrementar la variable cont
        result = funcion_b(a, b)
        print("Cantidad de veces llamada la función:", cont) #muestra las veces que se llamo a la funcion
        return result

    return funcion_c

@funcion_a
def suma(a, b):
    return a + b

print(suma(1, 4))
