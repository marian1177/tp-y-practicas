
# Archivo reubicado para el ejercicio de administrador de contexto, llamado por el modulo adm2 de
# carpeta ADMContexto
def funcionajena(n):
    print (" Se trabaja con un bloque de codigo en otro modulo 'adm2b.py del directorio Abstraccion'  , calculo fibonacci:")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    print (f"variable {a} y variable {b}")
