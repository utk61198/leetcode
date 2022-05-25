#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans=False
        s=set()
        for item in nums:
            if item in s:
                ans=True
            else:
                s.add(item)
        return ans



# a much cleaner solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True
        
        