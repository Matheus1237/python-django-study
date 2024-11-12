# Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel_escopo_init = 'Otávio'
        print(variavel_escopo_init)

    def comendo(self, alimento):
        print(f'{self.nome} está comendo {alimento}.')


leao = Animal('Leão')
print(leao.nome)
leao.comendo('Laranja')