class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self, acelerar):
        if acelerar > 0:
            print(f"Teu carro tá a {acelerar} km/h")
        else:
            print("Teu carro ta parado vacilão")

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

meu_carro = Carro("Mercedes", "Rico", 2019)
        
print("Marca do carro:", meu_carro.get_marca())
print("Modelo do carro:", meu_carro.get_modelo())
print("Ano do carro", meu_carro.get_ano())

meu_carro.acelerar(0)
meu_carro.acelerar(50)



