# https://leetcode.com/problems/set-matrix-zeroes/
import itertools
from typing import List


# O(m+n) space complexity solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_set = set()
        col_set = set()
        for i, j in itertools.product(range(len(matrix)), range(len(matrix[0]))):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)
        for i, j in itertools.product(range(len(matrix)), range(len(matrix[0]))):
            if i in row_set or j in col_set:
                matrix[i][j] = 0


if __name__ == "__main__":
    obj = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    obj.setZeroes(matrix=matrix)
    print(matrix)


# 00 01 02 12 22 21 20 10 11
