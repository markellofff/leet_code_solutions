class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> [int]:
        count = 0
        ind = 1
        arr = [0 for i in range(num_people)]
        while candies > 0:
            f1 = (ind - 1) * num_people
            f2 = ind * num_people
            sum1 = (f1 * (f1 + 1)) // 2
            sum2 = (f2 * (f2 + 1)) // 2
            res = sum2 - sum1
            if res <= candies:
                count += 1
                candies -= res
                ind += 1
            else:
                i = 0
                term = ((ind - 1) * num_people) + 1
                while candies > 0:
                    if term <= candies:
                        arr[i] = term
                        i += 1
                        candies -= term
                        term += 1
                    else:
                        arr[i] = candies
                        i += 1
                        candies = 0
        for i in range(num_people):
            arr[i] += ((count * (i + 1)) +
                       (num_people * (count * (count - 1)) // 2))
        return arr


test = Solution()

print(test.distributeCandies(10, 3))

