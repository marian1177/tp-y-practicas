def division(n1, n2):
    
    if n2==0:
        raise Exception("error en digito 2 es cero")

    else:
        return n1/n2

try:
    division(3,6)
except ValueError:
    print(ValueError)

n1=int(input("ingrese n1"))
n2=int(input("ingrese n2"))

print(division(n1,n2))