class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # memo = {}
        # def dfs(index):
        #     if index == n:
        #         return 1
        #     if s[index] == '0':
        #         return 0

        #     if index in memo:
        #         return memo[index]
            
        #     res = dfs(index+1)

        #     if index+1 < n and 10 <= int(s[index:index+2]) <= 26:
        #         res += dfs(index+2)
        #     memo[index] = res
        #     return memo[index]
        # return dfs(0)

        dp = [1]*(n+1)
        for i in range(n-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i <= n-2 and (s[i] =='1' or s[i] == '2' and s[i+1] in '0123456'):
                dp[i] += dp[i+2]
        return dp[0]
            