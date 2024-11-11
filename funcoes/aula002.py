def multiplicar(*args):
    
    total = 1
    for numeros in args:
        total *= numeros
    return total

numeros_testes = multiplicar(3, 5)
print(numeros_testes)


def par_ou_impar(a):

    if a % 2 == 0:
        return 'Par'
    return 'Ímpar'

num_teste = par_ou_impar(2)
print(num_teste)