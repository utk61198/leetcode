# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_sum=(len(nums)*(len(nums)+1))/2
        for item in nums:
            n_sum-=item
        return int(n_sum)


