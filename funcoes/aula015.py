# List comprehension em Python
# Forma rápida de criar listas a partir de iteráveis

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)



lista = []

for numero in range(11):
    lista.append(numero)

print(lista)

lista = [
    numero * 2 
    for numero in range(11)
]

print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 40},
    {'nome': 'p3', 'preco': 50},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 20
]

#print(novos_produtos)
#print(*novos_produtos, sep='\n')

p(novos_produtos)


# Filtro

lista1 = [n for n in range(11) if n < 5]
print(lista1)
