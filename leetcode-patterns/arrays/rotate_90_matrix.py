# https://leetcode.com/problems/rotate-image/


from typing import List
import itertools
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # transposing the matrix
        for i, j in itertools.product(range(m), range(n)):
            if i <= j:
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # reversing the transposed matrix
        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]


if __name__ == "__main__":
    obj = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    obj.rotate(matrix=matrix)
    print(matrix)