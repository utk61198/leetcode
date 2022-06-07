
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import List

# binary search solution, the question constraints says that peak element is guaranteed


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        h = len(arr) - 1

        while l < h:
            m = (l + h) // 2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m-1] > arr[m]:
                h = m
            elif arr[m+1] > arr[m]:
                l = m + 1
        return -1
