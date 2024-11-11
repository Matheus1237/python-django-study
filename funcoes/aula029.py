# Variáveis livres + nonlocal - não está definida no escopo da interna

'''def fora(x):
    a = x
    def dentro():
        print(locals())
        print(dentro.__code__.co_freevars)
        return a
    return dentro

dentro1 = fora(10)
print(dentro1())'''

# Essa é uma aplicação de closures em Python,
# onde a função interna dentro captura o
# ambiente da função externa fora.

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar   # valor_final não é uma variável desse escopo, so é possível ler
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('o'))
