import random



numero= 10

def primos(numero):
   total = 0
   cont=0 # se utiliza un contador dee divisores para saber si es primo
   for n in range(1, numero + 1):  #doble iteracion para tomar el rango del numero y el rango de divisores
       for d in range(1, n + 1):
           if n % d == 0:  # si el resto modulo de la division es cero encontro divisor
               cont+=1         
       if cont == 2:  # si el contador es 2 quiere decir que solo se divide por 1 y por si mismo
           print (f"el numero {n} es primo y se suma")
           total= total+n
       cont = 0 #se reinicia el contador para el siguiente ciclo
   print ("total",total)


primos(numero)