# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for item in nums:
            if nums[abs(item)-1]>0:
                nums[abs(item)-1]=-1*(nums[abs(item)-1])
        ans=[]
        for i,v in enumerate(nums):
            if v>0:
                ans.append(i+1)
        return ans