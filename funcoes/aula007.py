# Manipulando chaves e valores em dicionários

pessoa = {}

pessoa['nome'] = 'Matheus Antunes'
pessoa['idade'] = 20

print(pessoa['nome'])

del pessoa['idade']

print(pessoa)


if pessoa.get('idade'):
    print(pessoa['idade'])
else:
    print('NÃO EXISTE')
