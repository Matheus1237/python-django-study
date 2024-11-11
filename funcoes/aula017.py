# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta',
    'preco': '2.5',
    'categoria': 'Escritório',
}

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor 
    in produto.items()
    # Filtro
    if chave == 'categoria'
}

print(dc)

# isinstance verifica se um objeto pertence a instância de uma classe (Ex: int, str, float)


# SET

s1 = set(range(10))
print(s1)

s2 = {i * 2 for i in range(10)}
print(s2)
