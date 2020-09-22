class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_series = [0, 1, 1]
        if n <= 2:
            return tribonacci_series[n]
        else:
            for i in range(3, n + 1):
                next_term = tribonacci_series[i - 1] + tribonacci_series[i - 2] + tribonacci_series[i - 3]
                tribonacci_series.append(next_term)
            return tribonacci_series[n]


test = Solution()

print(test.tribonacci(3))
