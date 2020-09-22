class Solution:
    def maxPower(self, s: str) -> int:
        current_max = 1
        longest = 1
        for i in range ((len(s) -1)):
            if s[i] == s[i+1]:
                current_max+=1
            else:
                current_max = 1
            longest = max(current_max, longest)

        return longest


test = Solution()
print(test.maxPower("abbcccddddeeeeedcba"))
