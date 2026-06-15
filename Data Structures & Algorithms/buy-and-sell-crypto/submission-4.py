class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minb=prices[0]

        for price in prices:
            maxp=max(maxp,price-minb)
            minb=min(minb, price)
        return maxp