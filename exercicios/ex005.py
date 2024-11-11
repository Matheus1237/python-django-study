def contar_ocorrencias(lista, num):

    contador = 0

    for n in lista:
        if n == num:
            contador += 1

    return f'O número {num} apareceu {contador} vezes.' 


resultado = contar_ocorrencias([1, 2, 3, 2, 1, 4], 2)
print(resultado)


def soma(x, y):
    resultado = x + y
    print(resultado)


soma(2, 2)