class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def dfs(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if i > m-1 or j > n-1:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1
            
        #     memo[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
        #     return memo[(i,j)]
        # return dfs(0,0)
        dp = [1]*(n)
        new = dp
        for i in range(m-1):
            for j in range(1,n):
                new[j] = dp[j] + new[j-1]
            new,dp = dp,new
        return new[-1]

