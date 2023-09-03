class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def get_saldo(self):
        return self.saldo

    def get_titular(self):
        return self.titular

# Exemplo de uso
minha_conta = ContaBancaria("João", 1000.0)

print("Titular da conta:", minha_conta.get_titular())
print("Saldo inicial:", minha_conta.get_saldo())

minha_conta.depositar(500.0)
minha_conta.sacar(200.0)
