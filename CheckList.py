Lista_De_Tarefas = []

while True:
    opção = input("Seja bem-vindo ao CheckList Tarefas\n1- Adicionar tarefa\n2-Consultar tarefas\n3-Concluir tarefa\n4-Sair\nOque deseja fazer :")
    if opção == "1":
            while True:
                Verificação = input("Deseja adicionar uma tarefa (S/N): ").upper()
                if Verificação == "N":
                    print("Tarefas adicionadas")
                    print("-"*20)
                    break
                elif Verificação == "":
                    print("Você não digitou nada")
                else:
                    Tarefa = input("Adicionar tarefa: ")
                    while Tarefa == "":
                        print("Você não digitou nada")
                        Tarefa = input("Adicionar tarefa: ")
                    Lista_De_Tarefas.append(Tarefa)
                    # Enumerate faz a função de deixar os itens numerados
                    for i, item in enumerate(Lista_De_Tarefas):
                        print(f"{i + 1}. {item}")
    elif opção == "2":
        if len(Lista_De_Tarefas) == 0:
            print("Nenhuma tarefa foi adicionada")
            print("-"*20)
        else:
            for i, item in enumerate(Lista_De_Tarefas):
                print(f"{i + 1}. {item}")
                print("-" * 20)


    elif opção == "3":
        for i, item in enumerate(Lista_De_Tarefas):
            print(f"{i + 1}. {item}")
            print("-"*20)
        escolha = input(f"Digite o número da tarefa (de 0 a {len(Lista_De_Tarefas)-1}) que deseja encerrar ou aperte 'Enter' caso tenha terminado: ")
        try:
            valor = int(escolha)
            del Lista_De_Tarefas[valor]
            for i, item in enumerate(Lista_De_Tarefas):
                print(f"{i + 1}. {item}")
                print("-" * 20)
        except ValueError:
            print("Encerrado")

    elif opção == "4":
        print("Obrigado por usa a minha aplicação, volte sempre...")
        print("Saindo...")
        print("-"*20)
        exit()

    else:
        print("Opcão inválida")


#OBS:
    #Tentar adicionar essa aplicação em uma interface para que seja funcional e bonitinha



