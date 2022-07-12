
# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        for i in range(1, n+1):
            arr[i] = arr[i//2] + i % 2
        return arr

if __name__ == '__main__':
	obj = Solution()
	print(obj.countBits(5))
