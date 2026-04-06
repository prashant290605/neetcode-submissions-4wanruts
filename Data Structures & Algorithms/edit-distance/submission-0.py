class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        memo = {}
        def dfs(i,j):
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i] == word2[j]:
                memo[(i,j)] = dfs(i+1,j+1)
            else:
                rep = 1 + dfs(i+1,j+1)
                ins = 1 + dfs(i,j+1)
                dlt = 1 + dfs(i+1,j)
                memo[(i,j)] = min(rep,ins,dlt)
            return memo[(i,j)]
        return dfs(0,0)