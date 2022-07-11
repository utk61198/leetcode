# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	dp = [0]*len(nums)
    	dp[0] = nums[0]
    	ans = dp[0]
    	for i in range(1,len(nums)):
    		if dp[i-1] > 0:
    			dp[i] = nums[i] + dp[i-1]
    		else:
    			dp[i] = nums[i]
    		
    		ans = max(dp[i],ans)

    	return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
