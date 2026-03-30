class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0
        for p in prices:
            minPrice = min(minPrice,p)
            maxPrice = max(p-minPrice, maxPrice)
        return maxPrice        