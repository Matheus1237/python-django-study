
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True

        else:
            return False
            

solution = Solution()

numero_teste = solution.isPalindrome(12)
print(numero_teste)