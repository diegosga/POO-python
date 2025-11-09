class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo


    def set_titular(self, titular):
        self._titular = titular

    @property
    def get_titular(self):
        return self._titular
    

    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero):
        self._numero = numero
    
    @property
    def get_saldo(self):
        return self._saldo
    
    def depositar(self, saldo):
        if self._saldo == 0:
            self._saldo = saldo
        elif self._saldo > 0:
            self._saldo+= saldo
        else:
            raise ValueError("Saldo não pode ser negativo")
        
    def set_saldo(self, saldo):
        if self._saldo >= 0:
            self._saldo = saldo
        else:
            raise ValueError("Saldo não pode ser negativo")

    def sacar(self, saque):
        if self._saldo == 0 or self._saldo - saque<0:
            print("Impossivel sacar no momento")
        else:
            saldo_novo=self._saldo-saque
            self.set_saldo(saldo_novo)
        
        
