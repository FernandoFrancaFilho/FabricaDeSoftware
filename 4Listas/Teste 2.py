fila_de_tarefas = []
while True:
    print("Digite o que fazer:")
    print("1. Adicionar tarefa")
    print("2. Executar fila de tarefas")
    print("3. Sair")

    escolha = input("Escolha uma opção:")

    if escolha == '1':
        tarefa = input("Digite a descrição da tarefa:")
        fila_de_tarefas.append(tarefa)
        print("Tarefa" ,tarefa, "adicionada a fila.")
    elif escolha == '2':
        if fila_de_tarefas:
                tarefa = fila_de_tarefas.pop(-1)
                print("Executando:", tarefa)
        else:
                print("A fila de tarefas está vazia.")
    elif escolha == '3':
        break
    else:
        print("Opção inválida. Escolha novamente.")
