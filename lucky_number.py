class Solution:
    def findLucky(self, arr: []) -> int:
        length = len(arr)
        sorted_arr = sorted(arr)
        retuning_arr = []
        for i in range(length):
            if sorted_arr[i] <= length:
                if sorted_arr[i] == sorted_arr.count(sorted_arr[i]):
                    retuning_arr.append(sorted_arr[i])
        if len(retuning_arr) == 0:
            return -1
        else:
            return max(retuning_arr)


x = [5, 2, 2, 5]
test = Solution()
print(test.findLucky(x))
