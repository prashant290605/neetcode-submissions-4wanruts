class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def dfs(word,index):
            word += s[index]
            if index >= n-1:
                if word in wordDict:
                    return True
                else:
                    return False
            
            if (index,word) in memo:
                return memo[(index,word)]
            
            if word in wordDict:
                memo[(index,word)] = (True and dfs('',index+1)) or dfs(word,index+1)
            
            else:
                memo[(index,word)] = dfs(word,index+1)
            return memo[(index,word)]
        
        return dfs('',0)