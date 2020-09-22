class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)
        binary = binary[2:]
        complement = ''.join(list(map(lambda num: '1' if num == '0' else '0', binary)))
        return int(('0b'+complement), 2)

test = Solution()
print(test.bitwiseComplement(10))

