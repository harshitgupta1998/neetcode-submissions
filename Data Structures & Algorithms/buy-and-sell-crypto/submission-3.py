class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        r=1
        for i in range(len(prices)-1):
            if prices[r]<prices[l]:
                l=r
                r+=1
            else:
                profit=max(profit,(prices[r]-prices[l]))
                r+=1
        return profit