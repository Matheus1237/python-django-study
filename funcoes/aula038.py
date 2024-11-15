# Funções recursivas e recursividade
# funções que podem se chamar de volta
# úteis p/ dividir problemas grandes em partes menores

# Toda função recursiva deve ter
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão

def recursiva(inicio=0, fim=10):

    # Caso base
    if inicio >= fim:
        return fim

    # Contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())
