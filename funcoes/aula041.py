# Problema dos parâmetros mutáveis em funções python

def adiciona_clientes(nome, lista=[]): # Não usar valores mutáveis!!!
    lista.append(nome)
    return lista



clientes1 = adiciona_clientes('matheus')
clientes2 = adiciona_clientes('Pedro')
adiciona_clientes('Beatriz', clientes1)
print(clientes1)
