class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0
        diff = 0
        for p in prices:
            minPrice = min(minPrice,p)
            maxPrice = max(maxPrice,p)
            diff = max(p-minPrice, diff)
            if diff < 0:
                diff = 0
        return diff        