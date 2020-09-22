class Solution:
    def sumEvenAfterQueries(self, A: [], queries: [[]]) -> []:
        result = []
        for i in queries:
            A[i[1]] = int(A[i[1]]) + int(i[0])
            result.append(sum(list(filter(lambda x: x % 2 == 0, A))))
        return result


test = Solution()
print(test.sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))