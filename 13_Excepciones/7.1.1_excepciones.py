def division(n1, n2):
    if n2 == 0:
         raise ValueError("error en digito 2 es cero")

    return n1/n2


n1 = int(input("ingrese n1"))
n2 = int(input("ingrese n2"))

try:

    division(n1, n2)
except ValueError:
    
        print (ValueError)


print("division de lo ingresado es:", division(n1, n2))
