class FormaGeometrica:
    def calcular_a_área(self, raio):
        return 3.14 * (raio ** 2)


class Circulo(FormaGeometrica):
    pass


class Retangulo(FormaGeometrica):
    def calcular_a_área(self, base, altura):
        return base * altura


class Quadrado(Retangulo):
    pass


circulo = Circulo()
area = circulo.calcular_a_área(20)
print(area)

retangulo = Retangulo()
area = retangulo.calcular_a_área(5, 10)
print(area)

quadrado = Quadrado()
area = quadrado.calcular_a_área(2, 2)
print(area)