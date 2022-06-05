# https://leetcode.com/problems/first-missing-positive/

from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    p = 0
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1
    nums = nums[p:n]
    if nums:
        maxm = max(nums)

        for item in nums:
            if abs(item) - 1 < len(nums) and nums[abs(item)-1]>0:
                nums[abs(item)-1] = -1*nums[abs(item)-1]

        ans = 0

        for i, v in enumerate(nums):
            if v > 0:
                ans = i+1
                break

        return maxm+1 if ans == 0 else ans
    else:
        return 1


if __name__ == '__main__':
    print(firstMissingPositive([1,1]))
