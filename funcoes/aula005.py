def criar_multiplicador(operacao):

    def multiplicar(numero):
        return numero * operacao
    return multiplicar


duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadriplica = criar_multiplicador(4)

n = 5

print(duplica(n))
print(triplica(n))
print(quadriplica(n))
