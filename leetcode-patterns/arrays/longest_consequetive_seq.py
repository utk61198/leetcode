from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        ans = 0
        for item in nums:
            # if a smaller element is present in the hash set we don't count from the current element
            if item-1 not in hash_set:
                temp = item
                # while the new incremented element is present keep on going and finally take the max count
                while temp in hash_set:
                    temp = temp + 1
                ans = max(ans, temp - item)
        return ans


if __name__ != '__main__':
    pass
else:
    obj = Solution()
    input_list = [100, 4, 200, 1, 3, 2,5]
    print(obj.longest_consecutive(input_list))
