class Solution:
    def kWeakestRows(self, mat: [], k: int) -> [int]:
        result = {}
        for i in range(len(mat)):
            result[i] = mat[i].count(1)
        return list(dict(sorted(result.items(), key=lambda x: x[1])).keys())[0:k]


test = Solution()

test_mat = [[1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1]]

k = 3
print(test.kWeakestRows(test_mat, k))

