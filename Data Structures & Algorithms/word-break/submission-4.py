class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)
        memo = {}
        def dfs(index):
            if index == n:
                return True
            
            if index in memo:
                return memo[index]

            for i in range(index+1,n+1):
                if s[index:i] in wordset and dfs(i):
                    memo[index] = True
                    return True
            memo[index] = False
            return memo[index]
        
        return dfs(0)