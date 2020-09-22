from math import log


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> [int]:
        number = []
        i = 0
        while x ** i <= bound and i <= log(bound) + 1:
            j = 0
            while j <= bound and y ** j <= bound:
                sum = x ** i + y ** j
                if sum > bound:
                    break
                number.append(sum)
                j += 1
            i += 1
        return list(set(number))


test = Solution()
print(test.powerfulIntegers(1, 2, 100000))
