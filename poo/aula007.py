import json

CAMINHO_ARQUIVO = 'poo/aula007.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Beatriz', 18)
dados = vars(p1)

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)