class Animal:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def emitir_som(self):
        pass  # Método a ser implementado pelas subclasses

    def informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Raça: {self.raca}")

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca)
        self.raca = raca

    def emitir_som(self):
        return "Au Au!"

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca)
        self.raca = raca

    def emitir_som(self):
        return "Miau!"

# Exemplo de uso
cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mittens", 2, "Preto")

animais = [cachorro, gato]

for animal in animais:
    animal.informacoes()
    print(animal.emitir_som())
    print()
