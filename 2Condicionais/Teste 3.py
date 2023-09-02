num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))

if num1 > num2 and num3:
    print("O primeiro é o maior")

elif num2 > num3 and num1:
    print("O segundo é o maior")

elif num3 > num1 and num2:
    print("O terceiro é o maior")

else:
    print("Todos os números tem o mesmo valor")
