# raise - lançando exceções (erros)


# raise ValueError('Deu erro')

def nao_aceito_zero(d):

    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')


def deve_ser_int_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float!')


def divide(n, d):

    deve_ser_int_float(n)
    deve_ser_int_float(d)

    nao_aceito_zero(d)
    return n / d


teste = divide(3, 'a')
print(teste)
