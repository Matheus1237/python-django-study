# Estrutura de dados JSON
# Salvando dados em JSON

import json

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula040.json', 'w') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo,
#         indent=2
#         )

# Transformar o JSON no python

with open('aula040.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa['nome'])