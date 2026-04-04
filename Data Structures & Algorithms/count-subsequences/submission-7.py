class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [0 for _ in range(m+1)] 
        dp[m] = 1
        new = dp[:]


        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                new[j] = dp[j]
                if s[i] == t[j]:
                    new[j] += dp[j+1]
            dp = new[:]
        return dp[0]