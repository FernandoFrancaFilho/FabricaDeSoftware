class ContaBancaria():
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):


    def sacar(self, valor):
        if  valor > self.saldo:
            return print(f'{self.titular} não pode sacar o valor por saldo insuficiente.')
        else:
            self.saldo -= valor


    def get_saldo(self):
        return self.saldo

    def get_titular(self):
        return self.titular

minha_conta = ContaBancaria("João", 1000.0)

print("Titular da conta:", minha_conta.get_titular())
print("Saldo inicial:", minha_conta.get_saldo())

minha_conta.depositar(500.0)
minha_conta.sacar(1,200.0)


def sacar(self, valor):
    if 0 < valor <= self.saldo:
        self.saldo -= valor
        print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
