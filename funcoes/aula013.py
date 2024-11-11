
def executa(funcao, *args):
    return funcao(*args)


# Função lambda para somar dois valores

print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
)


# Função lambda para criar um multiplicador e outra função
# interna para multiplicar

duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(5))
