
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
            # id mid is 0 of last index and it is a peak one return mid
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums) - 1 and nums[mid] > nums[mid-1]):
                return mid
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            # if the element to the right is greater than mid, then the right half will always have a peak element  
            elif nums[mid+1] > nums[mid]:
                low = mid + 1

            # if the element to the left is greater than the mid, then the left half will always have the peak element
            elif nums[mid-1] > nums[mid]:
                high = mid - 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.findPeakElement([1, 2]))
