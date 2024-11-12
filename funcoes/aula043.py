# Controlando a quantidade de argumentos posicionais e nomeados em funções

def soma(x, y, /, a):
    return x + y

soma1 = soma(2, 5, a=3)
print(soma1)
