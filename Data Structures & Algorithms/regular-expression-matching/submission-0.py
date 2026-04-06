class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        memo = {}

        def dfs(i,j):
            
            if (i,j) in memo:
                return memo[(i,j)]

            if j == n:
                return i == m
            
            first_match = i < m and (s[i] == p[j] or p[j] == '.')

            if j+1 < n and p[j+1] == '*':
                ans = dfs(i,j+2) or (first_match and dfs(i+1,j))
            else:
                ans = first_match and dfs(i+1,j+1)
            memo[(i,j)] = ans
            return memo[(i,j)]
        return dfs(0,0,)