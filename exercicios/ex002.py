import string


class Solution:
    def contar_palavras(self, texto):

        texto_sem_pontuacao = texto.translate(str.maketrans('', '', string.punctuation))

        texto_sem_pontuacao = texto_sem_pontuacao.lower()

        palavras = texto_sem_pontuacao.split()

        contagem = {}
        for palavra in palavras:
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1

        palavra_mais_frequente = ''
        max_contagem = 0

        for palavra, cont in contagem.items():
            if cont > max_contagem:
                max_contagem = cont
                palavra_mais_frequente = palavra
                print('Palavra mais frequente:', palavra_mais_frequente)
        
        return contagem


sol = Solution()

entrada = sol.contar_palavras("Olá, mundo! O mundo é bonito. Olá a todos.")
print(entrada)
