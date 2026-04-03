class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def dfs(index):
            if index == n:
                return 1
            if s[index] == '0':
                return 0

            if index in memo:
                return memo[index]
            
            res = dfs(index+1)

            if index+1 < n and 10 <= int(s[index:index+2]) <= 26:
                res += dfs(index+2)
            memo[index] = res
            return memo[index]
        return dfs(0)