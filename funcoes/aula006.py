# Tipo dict (dicionário) - { }
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor"
# Chave pode ser considerado o índice que representa
# algum valor. 
# dict e list são MUTÁVEIS

pessoa = {
    'nome': 'Matheus Silva Antunes',
    'idade': 20,
    'profissao': 'Programador',
    'enderecos': [
        {'rua': 'Jazmin', 'numero': 14},
        {'rua': 'Cecília', 'numero': 29},
    ],
}

print(pessoa['nome'], type(pessoa))

print(pessoa['enderecos'])

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
