from aula027 import produtos
import copy

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}  # round diminui as casas decimais
    for p in copy.deepcopy(produtos)
]

print(*novos_produtos, sep='\n')

print()

produtos_ordenados_por_nome_decrescente = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print(*produtos_ordenados_por_nome_decrescente, sep='\n')
