

# https://leetcode.com/problems/house-robber-ii/


# this problem is similar to house robber 1, we just can't rob the first and last house together
# so get the answer in each case and take the max of them
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def linear_rob(nums):
            if len(nums) == 1:
                return nums[0]
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1]= max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-2] + nums[i],dp[i-1])
            return dp[len(nums)-1]
            
        return max(linear_rob(nums[1:]),linear_rob(nums[:-1]))
    