cadena=str(input("ingrese una cadena que represente un numero "))
print("la cadena ingresada fue: ", cadena)

try:
    int(cadena)
except:
    print("error tenia que ser un numero")