class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            a = float('inf')
            for i in coins:
                if amount - i < 0:
                    continue
                res = dfs(amount-i)
                if res != -1:
                    a = min(a,1+res)
            if a == float('inf'):
                memo[amount] = -1
            else:
                memo[amount] = a
            return memo[amount]
        return dfs(amount)
    