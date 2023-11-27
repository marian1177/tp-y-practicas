class CuentaBancaria:
    def __init__(self,titular):
        self.titular = titular
        #valor por default del atributo a trabajar
        self._saldo = 0  

    @property  
    #dato sensible protegido         
    def obtener_saldo(self):
        return f"su saldo actual es {self._saldo}"
    
    def depositar(self,monto):   
        #metodo de modificacion donde se suma importe (validando billetes multiplos de 100 unicamente)
        if monto > 0 and monto  % 100 == 0:
            self._saldo += monto
            return f"su saldo actual es {self._saldo}"
        else:
            return "ocurrio un error en el ingreso de monto"

    def retirar(self,monto):  
        #metodo de modificacion donde se resta importe (validando billetes multiplos de 100 unicamente)
        if self._saldo > 0 and monto % 100 == 0:
            self._saldo -= monto
            return f" usted retiro efectivo, su saldo actual es {self._saldo}"
        else:
            return "ocurrio un error en el ingreso de monto a retirar"

#instancia de prueba
user = CuentaBancaria("mariano")
print(user.depositar(3000))
print(user.retirar(40))
print(user.retirar(400))
print(user.obtener_saldo)