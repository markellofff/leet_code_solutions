class Solution:
    def repeatedNTimes(self, A: [int]) -> int:
        res = {}
        for num in set(A):
            res[num] = A.count(num)
        return list(res.keys())[list(res.values()).index(max(res.values()))]


test = Solution()
print(test.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))