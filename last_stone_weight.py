# it will give the TLE while submitting on Leetcode

class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            print(stones)
            if stones[0] > stones[1]:
                rock = stones[0] - stones[1]
                stones[0], stones[1] = rock, 0
            elif stones[0] == stones[1]:
                stones[0] = stones[1] = 0
                stones = list(filter(lambda a: a != 0, stones))
        return stones[0] if len(stones) == 1 else 0


test = Solution()
print(test.lastStoneWeight([2, 7, 4, 1, 8, 1]))
