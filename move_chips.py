class Solution:
    def minCostToMoveChips(self, position: [int]) -> int:
        odd = 0
        even = 0
        for i in range(len(position)):
            if position[i] % 2 != 0:
                odd += 1
            else:
                even += 1
        return min(odd, even)


test = Solution()
print(test.minCostToMoveChips([1,2,2,2,2]))
