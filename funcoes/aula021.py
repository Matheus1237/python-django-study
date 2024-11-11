# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()

for iter in iterator:
    print(iter)

# A única coisa que o iterator faz é mostrar o próximo objeto


# Generator Expression - Todo Generator é um Iterator mas não 
# ao contrário

# Sabe pausar

generator = (n for n in range(100000)) # Generator Expression
print(sys.getsizeof(generator))


# Mesmo aumentando o valor, no generator ele mantém o valor dos dados
# Diferença da lista - não é possível acessar índices nem o len

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
