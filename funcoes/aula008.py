# Métodos úteis dos dicionários

# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com chaves e valores
# items - chave e valor
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy) - não copia subníveis
# get - obtém uma chave
# pop - printa a chave e depois apaga
# popitem - elimina a última chave do dicionário
# update - atualiza um dicionário com outro

import copy # deep copy


pessoa = {
    'nome': 'Matheus Silva Antunes',
    'idade': 20,
    'profissao': 'Programador',
    'lista1': [2, 4, 7]
}

print(len(pessoa)) # ou __len__
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa2 = pessoa.copy()
pessoa2['lista1'][1] = 100 
print(pessoa2)

print(pessoa.get('nome'))

print(pessoa.pop('nome'))
print(pessoa)

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

pessoa.update({
    'nome': 'Beatriz de Oliveira',
    'religiao': 'Evangélica',
})
# OU
pessoa.update(nome='Davi', nacionalidade='Brasileiro')

print(pessoa)
