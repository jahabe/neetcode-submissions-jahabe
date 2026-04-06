class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        best = 0

        for p in prices:
            minPrice = min(minPrice, p)
            best = max(best, p - minPrice)
        return best