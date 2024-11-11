# Números Fibonacci

# 1 1 2 3 5 8 13 ...

def fibonacci(qtd_elementos):

    lista_soma = [0, 1]
    
    for n in range(2, qtd_elementos):
        soma = lista_soma[-1] + lista_soma[-2] # Acessa o último e o pnúltimo n da lista.
        lista_soma.append(soma)
        




    print(lista_soma)


fibonacci(11)