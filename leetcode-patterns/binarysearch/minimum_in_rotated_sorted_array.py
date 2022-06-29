
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
    	if len(nums) == 1: return nums[0]
    	low = 0
    	high = len(nums) - 1
    	while low <= high:
    		mid = (low + high) // 2

    		# if the mid is the first element, check if the next element is greater
    		if mid == 0 and nums[mid+1] > nums[mid]:
    			return nums[mid]

    		# if mid is the last element, check if the element before is bigger
    		if mid == len(nums) - 1 and nums[mid-1] > nums[mid]:
    			return nums[mid]

    	    # the smallest element in a roated array will be smaller than it's neighbor elements
    		if nums[mid-1] > nums[mid] < nums[mid+1]:
    			return nums[mid]

    		# mid is greater than the high that means the smallest element is in the right half, otherwise the left half
    		elif nums[mid] > nums[high]:
    			low = mid + 1
    		else:
    			high = mid - 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.findMin([2,1]))
