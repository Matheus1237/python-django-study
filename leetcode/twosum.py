# nums = [2,7,11,15] target = 9 Esperado = [0, 1]

class Solution:
    def twoSum(self, nums, target):
            num_dict = {}

            for i, num in enumerate(nums):
                complemento = target - num

                if complemento in num_dict:
                        return [num_dict[complemento], i]

                num_dict[num] = i


solution = Solution()

resultado = solution.twoSum([2,7,11,15], 9)

print(resultado)
