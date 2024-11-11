# Exercício 1: Gerenciador de Contatos
# Objetivo: Criar um gerenciador de contatos que armazene 
# informações de pessoas em um dicionário.

# Defina uma função adicionar_contato(nome, telefone) que 
# adiciona um novo contato a um dicionário de contatos. 
# O nome deve ser a chave e o telefone o valor.
# Defina uma função remover_contato(nome) que remove um 
# contato pelo nome.
# Defina uma função listar_contatos() que imprime todos 
# os contatos armazenados.
# Adicione tratamento de erros para lidar com casos em 
# que um contato não existe ao tentar removê-lo.
# Use um loop while para permitir que o usuário adicione, 
# remova ou liste contatos até que escolha sair do programa.
# Utilize um gerenciador de contexto para salvar os contatos 
# em um arquivo quando o programa é encerrado.


contatos = {}

class GerenciadordeContatos:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __enter__(self):
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    nome, telefone = linha.strip().split(', ')
                    contatos[nome] = telefone
        except FileNotFoundError:
            pass        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.nome_arquivo, 'w') as arquivo:
            for nome, telefone in contatos.items():
                arquivo.write(f'Nome: {nome}| Telefone: {telefone}\n')

nome_arquivo = 'contatos.txt'

def adicionar_contato():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    contatos[nome] = telefone


def remover_contato():
    while True:
        contato = input('Nome do contato que quer remover: ')
        
        if contato not in contatos:
            print('Contato não existe, tente novamente.')
        else:
            contatos.pop(contato)
            print(f'Contato {contato} removido com sucesso.')
            break


def listar_contatos():
    for nome, telefone in contatos.items():
        print(f'Nome: {nome} Telefone: {telefone}')

nome_arquivo = 'contatos.txt'

with GerenciadordeContatos(nome_arquivo):
    while True:
        print('='*23)
        print('Gerenciador de Contatos')
        print('='*23)

        acao = input('(1)Adicionar contato\n(2)Remover contato\n(3)Listar contatos\n(4)Sair\nEscolha uma opção: ')
        print()

        if acao == '1':
            adicionar_contato()

        elif acao == '2':
            remover_contato()

        elif acao == '3':
            listar_contatos()
            
        elif acao == '4':
            break

        else:
            print('Essa opção não existe.')
