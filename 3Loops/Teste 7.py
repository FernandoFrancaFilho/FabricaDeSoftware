total_masculino = 0
total_feminino = 0

while True:
    sexo = input("Digite o sexo (M/F) ou 'sair' para encerrar:")

    if sexo == "M":
        total_masculino += 1
    elif sexo == "F":
        total_feminino += 1
    elif sexo == "sair":
        break
    else:
        print("Opção invalida. Digite 'M','F' ou 'sair', seu primata.")

print("Total de masculino:", total_masculino)
print("Total de feminino:", total_feminino)
