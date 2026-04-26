class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        b=prices[0]
        for s in prices:
            maxp=max(maxp,s-b)
            b=min(b,s)
        return maxp