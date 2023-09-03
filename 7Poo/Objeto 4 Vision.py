import math

class FormaGeometrica:
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

retangulo = Retangulo(9, 12)
area_retangulo = retangulo.calcular_area()
print("Área do retângulo:", area_retangulo)

circulo = Circulo(9)
area_circulo = circulo.calcular_area()
print("Área do círculo:", area_circulo)
