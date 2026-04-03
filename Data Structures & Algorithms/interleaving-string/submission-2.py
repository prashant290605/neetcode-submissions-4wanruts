class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        n = len(s1)
        m = len(s2)
        def dfs(i,j):
            if i == n and j == m:
                return True
            
            if (i,j) in memo:
                return memo[(i,j)]
        
            res = False
            if i < n and s1[i] == s3[i+j]:
                res = dfs(i+1,j)
            if not res and j < m and s2[j] == s3[i+j]:
                res = dfs(i,j+1)
            
            memo[(i,j)] = res
            return memo[(i,j)]
        return dfs(0,0)