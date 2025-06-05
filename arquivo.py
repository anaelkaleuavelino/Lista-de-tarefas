lista_de_tarefas = []
continuar = True

while continuar: 
    print("Escolha uma opcao:\n" \
          " 1 - Inserir nova tarefa\n" \
          "2 - Lista de tarefas\n"
        "3 - Sair")
    opcao = input("insira o que deseja fazer: ")
    

    if opcao == "1":   
      tarefa = input('Insira uma nova tarefa')
      lista_de_tarefas.append(tarefa)
    elif opcao == "2": 
       print(lista_de_tarefas)
    elif opcao == "3":
      continuar = False
    else:
       print("Opção inválida! Tente novamente!")
    print('\n')
            