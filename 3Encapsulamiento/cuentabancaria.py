class CuentaBancaria:
    def __init__(self,titular):
        self.titular = titular
        self._saldo = 0

    @property
    def obtener_saldo(self):
        return f"su saldo actual es {self._saldo}"
    
    def depositar(self,monto):
        if monto > 0 and monto  % 100 == 0:
            self._saldo += monto
            return f"su saldo actual es {self._saldo}"
        else:
            return "ocurrio un error en el ingreso de monto"

    def retirar(self,monto):
        if self._saldo > 0 and monto % 100 == 0:
            self._saldo -= monto
            return f" usted retiro efectivo, su saldo actual es {self._saldo}"
        else:
            return "ocurrio un error en el ingreso de monto a retirar"


user = CuentaBancaria("mariano")
print(user.depositar(3000))
print(user.retirar(40))
print(user.retirar(400))
print(user.obtener_saldo)