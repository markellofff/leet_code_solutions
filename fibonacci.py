class Solution:
    def fib(self, N: int) -> int:
        fibonacci = [0, 1]
        if N == 0 or N == 1:
            return fibonacci[N]
        else:
            for i in range(2, N+1):
                fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
            return fibonacci[N]


test = Solution()
print(test.fib(3))
