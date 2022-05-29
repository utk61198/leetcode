
# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) >= 1:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            return fast
        else:
            return -1


if __name__ == "__main__":
    obj = Solution()
    print(obj.findDuplicate([1, 3, 4, 2, 2]))
# 1 3 4 2 2
# slow=1
# fast=3

# slow 3
# fast 4

# slow 2
# fast 4

# slow 4
# fast 4


# find the entry point of the cycle
# fast 0
# slow 4


# fast 1 slow 2
# fast 3 slow 4
# fast 2 slow 2
