'''
Higher Order Functions
Funções de Primeira Classe
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia', 'Matheus')
print(v)
