# https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix) - 1
        level = 0
        while l <= h:
            m = (l + h) // 2
            # check if target is somewhere in between the current level, then return current level
            if matrix[m][0] <= target <= matrix[m][len(matrix[0])-1]:
                level = m
                break

            # if target greater than first level of current level, change low
            elif target > matrix[m][0]:
                l = m + 1

            # if target smaller than first level of current level, change high 
            else:
                h = m - 1 

        # check if the target is the returned level
        if target in matrix[level]:
            return True
        else:
            return False