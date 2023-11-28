try:
    cadena = str(input("Ingrese una cadena que represente un número: "))
    print("La cadena ingresada fue:", cadena)

    if cadena.isdigit():
        numero = int(cadena)
        print("El número es:", numero)
    else:
        raise ValueError("Error, la cadena no representa un número válido.")

    
except ValueError :
    print(ValueError)
