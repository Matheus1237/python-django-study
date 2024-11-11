class Solution:
    def longestCommonPrefix(self, lista):
        
        prefixo_comum = lista[0]

        if not lista:
             return ''

        for palavra in lista[1:]:
                while not palavra.startswith(prefixo_comum):
                     prefixo_comum = prefixo_comum[:-1]
                     if not prefixo_comum:
                        return ''
        
        return prefixo_comum



sol = Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))