
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = len(arr)//2
        ans = arr[peak]
        
        while True:
            if peak == 0 or peak == len(arr) - 1:
                ans = peak
                break
            else:
                if arr[peak] > arr[peak-1] and arr[peak] > arr[peak+1]:
                    ans = peak
                    break
                elif arr[peak] > arr[peak-1] and arr[peak] < arr[peak+1]:
                    peak += 1
                else:
                    peak -= 1
        return ans