class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(count_open,count_close,s):
            if count_open == n and count_close == n:
                ans.append(s)
                return
            if count_open < n:
                dfs(count_open+1,count_close,s+'(')
            
            if count_close < n and count_close < count_open:
                dfs(count_open,count_close+1,s+')')
        dfs(0,0,'')
        return ans