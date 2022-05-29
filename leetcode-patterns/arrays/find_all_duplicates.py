import enum
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for item in nums:
            if nums[abs(item)-1] > 0:
                nums[abs(item)-1] = -1*abs(nums[abs(item)-1])
            else:
                ans.append(abs(item))

        return ans


if __name__ == "__main__":
    obj = Solution()
    list = [2, 2]
    print(obj.findDuplicates(list))
