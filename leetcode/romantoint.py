class Solution:

    def romanToInt(self, s: str) -> int:

        valores_romanos = {
                        'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000
                    }
        total = 0
        n = len(s)

        for i in range(n):
            valor_atual = valores_romanos[s[i]]

            if i < n - 1 and valores_romanos[s[i]] < valores_romanos[s[i + 1]]:
                total -= valor_atual
            else:
                total += valor_atual

        return total            


sol = Solution()

nroman = sol.romanToInt('III')
print(nroman)