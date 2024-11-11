import os

# Criando arquivos com Python
# Usamos a função open para abrir
# Modos:
# r (leitura) w (escrita) x (criação)
# a (escreve ao final)
# Context manager - with (abre e fecha)

caminho_arquivo = 'funcoes/aula040.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close() # Sempre lembrar de fechar o arquivo

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Atenção')
    arquivo.seek(0, 0) # Voltar o cursor para o início
    print(arquivo.read())

print('#' * 20)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

os.rename(caminho_arquivo, "novo_arquivo") # pode mover o arquivo também
os.unlink(caminho_arquivo) # ou remove
