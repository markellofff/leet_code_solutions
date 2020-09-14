class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if Solution.isPalindrome(s):
            return 1
        return 2

    def isPalindrome(self):
        # Start from leftmost and
        # rightmost corners of str
        l = 0
        h = len(self) - 1

        # Keep comparing characters
        # while they are same
        while h > l:
            if self[l] != self[h]:
                return 0
            l = l + 1
            h = h - 1

        return 1


test = Solution()
print(test.removePalindromeSub(""))