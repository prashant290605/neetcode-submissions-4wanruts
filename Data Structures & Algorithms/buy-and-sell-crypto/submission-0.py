class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        profit = 0
        max_profit = 0
        for i in range(n):
            buy = min(buy,prices[i])
            profit = max(prices[i]-buy,0)
            max_profit = max(profit,max_profit)
        return max_profit
