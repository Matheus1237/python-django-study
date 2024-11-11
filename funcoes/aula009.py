# Sets - Conjuntos em Python (tipo set)

# Mutáveis, mas só aceitam elementos imutáveis

# Não garante a ordem dos elementos

conjunto1 = set('Matheus')
print(conjunto1, type(conjunto1))

conjunto2 = {'Matheus', 2, 3, 'Bea'}
print(conjunto2)

# São úteis para remover valores duplicados

conjunto3 = {2, 3, 2, 2, 3} # retorno 2, 3
print(conjunto3)

# Remoção de duplicados na lista, transformando ela em um set dps
# voltando a ser lista

l1 = [1, 2, 1, 1, 1, 2, 2, 3, 3, 3, 3]
s1 = set(l1)
print(s1)
l2 = list(s1)
print(l2)

# Métodos úteis do set:

# add, update, clear, discard

s4 = set()
s4.add('Lanche')
s4.add(2)
s4.add((1, 2, 3))
print(s4) # {2, (1, 2, 3), 'Lanche'}

s4.update(('Olá Mundo', 2, 3))
print(s4)

s4.discard('Lanche') # Não tem índice, precisa passar o valor
print(s4)

print()
print()
print()

# Operações úteis

# União - | Une
# Interceção - & Itens presentes em amboas
# Diferença - (-) Itens presentes apenas no set da esquerda
# Diferença simétrica - ^ Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {4, 5, 6, 2}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
