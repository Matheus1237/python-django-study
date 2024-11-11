
def generator(n=0):
    yield 1 # Pausar
    return 'Acabou'


gen = generator(n=0)
print(next(gen)) # Aqui a função não foi executada completamente, foi pausada
print(next(gen)) # StopIteration: Acabou
