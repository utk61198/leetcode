

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        m=0
        while r<len(prices):
            if prices[r]-prices[l]>0:
                if prices[r]-prices[l]>m:
                    m=prices[r]-prices[l]
                r=r+1
            else:
                l=r
                r=r+1
        return m
            