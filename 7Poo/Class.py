class Garrafa:
    def __init__(self, tamanho, cor, marca):
            self.tamanho = tamanho
            self.cor = cor
            self.marca = marca
            

    def __str__(self):
        return f'oi eu sou uma garrafa {self.marca}'


garrafa = Garrafa(100, 'preto', 'shopee')
print(garrafa)

stanley = Garrafa(100, 'preto', 'stanley')
print(stanley)
