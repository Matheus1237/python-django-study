'''
*args - Argumentos não nomeados
Empacotamento e desempacotamento
'''

# Desempacotamento
x, y, *resto = 1, 2, 4, 5, 6

print(x, y, resto) # 1 2 [4, 5, 6]


def soma(*args): # args empacota dentro de uma tupla
    total = 0
    print(args, type(args)) # tuple

    for num in args:
        total += num
    return total


soma_teste = soma(1, 4, 8, 2, 3, 6, 7)
print(soma_teste)

#print(sum(4, 6, 5, 2, 1, 9))

# É possível desempacotar uma tupla com *variavel