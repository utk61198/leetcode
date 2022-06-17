
# https://leetcode.com/problems/find-peak-element/
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums) - 1 and nums[mid] > nums[mid-1]):
                return mid
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid+1] > nums[mid]:
                low = mid + 1
            elif nums[mid-1] > nums[mid]:
                high = mid - 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    obj.findPeakElement([1, 2])
