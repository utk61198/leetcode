# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    	n = len(matrix) - 1
    	m = len(matrix[0]) - 1
    	i = 0  
    	j = m
    	while i <= n and j >= 0:
    		if matrix[i][j] == target:
    			return True
    		elif target < matrix[i][j]:
    			j = j - 1
    		else:
    			i = i + 1
    	return False

    	


if __name__ == '__main__':
    obj = Solution()
    print(obj.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
          3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
