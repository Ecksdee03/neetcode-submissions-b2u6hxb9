class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minPrice = prices[0]
        diff = 0
        checkIndex = 0
        for i in range(len(prices)):
            if prices[i] > maxPrice:
                maxPrice = prices[i]
                checkIndex = i
            if prices[i] < minPrice:
                minPrice = prices[i]
            if maxPrice - minPrice > diff and checkIndex >= i:
                diff = maxPrice - minPrice
            if checkIndex < i:
                maxPrice = 0
        return diff