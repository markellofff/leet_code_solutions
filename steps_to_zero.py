class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                i += 1
            else:
                num = num - 1
                i += 1
        return i


test = Solution()
print(test.numberOfSteps(8))
