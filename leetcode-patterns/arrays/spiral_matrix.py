# https://leetcode.com/problems/spiral-matrix/
from typing import List


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    row_start, row_end = 0, len(matrix)-1
    col_start, col_end = 0, len(matrix[0])-1
    ans = []
    while row_start <= row_end and col_start <= col_end:

        for i in range(col_start, col_end+1):
            ans.append(matrix[row_start][i])
        row_start += 1

        for i in range(row_start, row_end+1):
            ans.append(matrix[i][col_end])
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start-1, -1):
                ans.append(matrix[row_end][i])
            row_end -= 1
        if col_start <= col_end:
            for i in range(row_end, row_start-1, -1):
                ans.append(matrix[i][col_start])
            col_start += 1

    return ans


if __name__ == '__main__':
    print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
