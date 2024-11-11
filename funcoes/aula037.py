
# reduce - faz a redução de um iterável em um valor
from functools import reduce

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 10},
    {'nome': 'Produto 2', 'preco': 105},
    {'nome': 'Produto 4', 'preco': 69},
]

# def funcao_do_reduce(acumulador, produto):
#     return acumulador + produto['preco']

total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0 # valor inicial
)

print(total)