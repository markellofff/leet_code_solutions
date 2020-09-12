class Solution:
    def isPalindrome(self, x: int) -> bool:
        # write your code here
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


test = Solution()
print(test.isPalindrome(121))
