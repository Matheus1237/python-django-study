# Função Lambda - anônimas (não possui nome) e de apenas uma linha

lista1 = [1, 3, 4, 6, 2, 5, 8, 0]

lista1.sort()
print(lista1)


lista2 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def ordena(item):
    return item['nome']


lista2.sort(key=ordena)

for item in lista2:
    print(item)


lista10 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print('')


# Utilizando a LAMBDA para não precisar criar um método

lista10.sort(key=lambda item: item['nome'])

# sorted faz uma cópia rasa
lista20 = sorted(lista10, key=lambda item: item['sobrenome'])

exibir(lista10)
exibir(lista20)
