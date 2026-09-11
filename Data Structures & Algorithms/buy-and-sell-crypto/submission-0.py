class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        length = len(prices)
        for i in range(length):
            if prices[r] < prices[l]:
                l = r
            profit = max(profit, prices[r] - prices[l])
            r += 1
        
        return profit