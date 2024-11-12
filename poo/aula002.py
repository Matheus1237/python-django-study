# Métodos em instâncias de classes Python
# Método é igual função, mas quando nos referimos como método, significa que é uma função dentro da classe

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca', 'Chevrolet')
print(fusca.nome, fusca.marca)
fusca.acelerar()