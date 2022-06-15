# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i == 0:
                arr = nums[1:]
            elif i == len(nums)-1:
                arr = nums[0:len(nums)-1]
            else:
                arr = nums[0:i] + nums[i+1:]
            
            ans = True
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    ans = False
            if ans:
                return True
        return False