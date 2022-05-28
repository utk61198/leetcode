
# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        temp = 1
        for item in nums:
            prefix.append(temp)
            temp = temp*item
        # 1 2 3 4
        # 1 1 2 6
        #
        # 4 3 2 1
        # 1 4 12 24
        # 24 12 4 1   postfix
        # 1   1  2 6 prfix
        # 24 12 8 6 prefix*postfixa

        temp = 1
        postfix = []
        for item in nums[::-1]:
            postfix.append(temp)
            temp = temp*item

        ans = []
        for a, b in zip(prefix, postfix[::-1]):
            ans.append(a*b)
        return ans
