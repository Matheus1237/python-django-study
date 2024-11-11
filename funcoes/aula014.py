# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Matheus',
    'sobrenome': 'Beatriz',
}

a, b = pessoa # Retorna as chaves
print(a, b)

a, b = pessoa.values() # Valores das chaves
print(a, b)

a, b = pessoa.items() # Chave e valor numa tupla
print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for key, value in pessoa.items():
    print(key, value)

pessoa2 = {
    'nome': 'Brenda',
    'sobrenome': 'Antunes',
}

dados = {
    'idade': 19,
    'altura': 1.80,
}

pessoa2_completa = {**pessoa2, **dados}
print(pessoa2_completa)

# kwargs - argumentos nomeados

def mostrar_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADO:', args)
    
    for key, value in kwargs.items():
        print(key, value)

mostrar_argumentos_nomeados(123, nome='Otávio', sobrenome='Miranda')

mostrar_argumentos_nomeados(**pessoa2_completa)
