from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:


    	def search_helper(nums, target, low, high):
            if low > high:
                return -1
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    return search_helper(nums, target, low, mid - 1)
                else:
                    return search_helper(nums, target, mid + 1, high)
            if nums[mid] < nums[high]:
            	if nums[mid] < target <= nums[high]:
            		return search_helper(nums, target, mid+1, high)
            	else:
                	return search_helper(nums, target, low, mid - 1)
    	if len(nums) == 1:
    		if target == nums[0]:
    			return 0
    		else:
    			return -1
    	ans = search_helper(nums,target,0,len(nums) - 1)
    	return ans if ans else -1



if __name__ == '__main__':
    obj = Solution()
    print(obj.search([4, 5, 6, 7, 0, 1, 2],0))
