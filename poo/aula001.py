# Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# pascalcase - class CriarBaseDeDados

class Pessoa: # classe é um molde que vai gerar novos objetos - Instâncias
    def __init__(self, nome, sobrenome):
        self.nome = nome # O self é como se fosse um p1 la de baixo, uma instância
        self.sobrenome = sobrenome


p1 = Pessoa('Matheus', 'Antunes') # Criando um instância da classe Pessoa

# p1.nome = 'Matheus'
# print(p1)

print(p1.nome, p1.sobrenome)