class Solution():
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pilha = []
        pares = {')': '(', ']': '[', '}': '{'}

        for p in s:
            if p in "({[":
                pilha.append(p)
            elif p in ")]}":
                if not pilha:
                    return False
                ultimo_aberto = pilha.pop()
                if ultimo_aberto != pares[p]:
                    return False
                
        return len(pilha) == 0        


s = Solution()
teste = s.isValid("()[]{")
print(teste)
