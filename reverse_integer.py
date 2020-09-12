class Solution:
    def reverse(self, x: int) -> int:
        # write your code here
        x = str(x)
        if x[0] == '-':
            rev = int('-' + x[-1:0:-1])
            if -2 ** 31 <= rev <= ((2 ** 31) - 1):
                return rev
            else:
                return 0
        else:
            rev = int(x[::-1])
            if -2 ** 31 <= rev <= ((2 ** 31) - 1):
                return rev
            else:
                return 0


test = Solution()
print(test.reverse(-123))
print(test.reverse(321))

