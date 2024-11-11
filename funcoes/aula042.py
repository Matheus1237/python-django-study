# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def lista_tarefas():
    todo = []
    item_removido = None

    while True:
        print()
        print('Comandos: [L]istar, [D]esfazer, [R]efazer, [F]echar')
        print()
        
        escolha = input("Digite uma tarefa ou um comando: ")
        print()
        
        if escolha == "L":
            print(todo)

        elif escolha == "D":
            if todo:
                item_removido = todo.pop()
            else:
                print('Não há tarefas na lista para remover.')

        elif escolha == "R":
            if item_removido is not None:
                todo.append(item_removido)
            else:
                print('Não há tarefas para remover.')
                
        elif escolha == "F":
            print('Fechando o programa...')
            break
        else:
            todo.append(escolha)
            print('Tarefa adicionada com sucesso!')


lista_tarefas()