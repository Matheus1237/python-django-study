def fatorial(n):

    resultado = 1

    for numero in range(2, n+1):
        resultado *= numero
    
    print(resultado)

fatorial(5)
