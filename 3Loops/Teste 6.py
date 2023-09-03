total = 0
numero = float(input("Digite um número (0 para parar): "))

while numero != 0:
    total += numero
    numero = float(input("Digite um número (0 para parar): "))

print("A soma dos números digitados é:", total)
