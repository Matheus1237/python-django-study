# __dict__ e vars para atributos de instância

class Pessoa:
    atributo = 'valor'      # Atributos da classe
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return f'{self.nome} nasceu em {Pessoa.ano_atual - self.idade}'
    

p1 = Pessoa('Matheus', 20)
print(p1.get_ano_nascimento())

# Onde os valores da instância estão armazenados?
p1.__dict__['profissão'] = 'programador'
print(p1.__dict__)
print(vars(p1))