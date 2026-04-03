class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dfs(index,last,last_ed):
            if (index,last_ed) in memo:
                return memo[(index,last_ed)]
            
            if index >= n:
                return 0
            if last == 1:
                x = prices[index] - prices[last_ed]
                memo[(index,last_ed)] = max(dfs(index+2,0,-1) + x,dfs(index+1,1,last_ed))
            else:
                memo[(index,last_ed)] = max(dfs(index+1,1,index),dfs(index+1,0,-1))

            return memo[(index,last_ed)]
        
        return dfs(0,0,-1)