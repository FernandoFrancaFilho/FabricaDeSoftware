def calculadora():
    def soma(a, b):
        print(a + b)
    def sub(a, b):
        print(a - b)
    def mult(a, b):
        print(a * b)
    def div(a, b):
        print(a / b)
    var = str(input('operacao:' ))
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    if var == 'soma':
        soma(num1, num2)
    elif var == 'subtracao':
        sub(num1, num2)
    elif var == 'multiplicacao':
        mult(num1, num2)
    elif var == 'divisao':
        div(num1, num2)
    else:
        print('operacao nao reconhecida')

calculadora()

