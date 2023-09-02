velocidade = float(input("Coloque sua velocidade: "))

limite = 80
multa = 7
passou = (velocidade - limite)*7

if velocidade > limite:
    print("Sua velocidade foi: ",velocidade, "Você pagará R$: ",passou)

else:
    print("Sua velocidade está no padrão")
