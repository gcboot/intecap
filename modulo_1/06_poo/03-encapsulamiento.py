class Cuenta:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad inválida")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente o cantidad inválida")