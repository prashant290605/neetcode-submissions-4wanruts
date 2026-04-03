class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, amt):
            if amt == 0:
                return 1
            if i == len(coins):
                return 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]
            
            take = 0
            if coins[i] <= amt:
                take = dfs(i, amt - coins[i])
            
            skip = dfs(i + 1, amt)
            
            memo[(i, amt)] = take + skip
            return memo[(i, amt)]

        return dfs(0, amount)