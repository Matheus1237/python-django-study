'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):

    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

retornar_bom_dia = criar_saudacao('Bom dia')
retornar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Matheus', 'Carlos']:
    print(retornar_bom_dia(nome))
    print(retornar_boa_noite(nome))
