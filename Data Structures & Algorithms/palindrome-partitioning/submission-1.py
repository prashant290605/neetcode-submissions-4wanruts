class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(idx,partition):
            if idx == len(s):
                ans.append(partition[:])
                return 
            for i in range(idx,len(s)):
                x = s[idx:i+1]
                if x == x[::-1]:
                    partition.append(x)
                    dfs(i+1,partition)
                    partition.pop()
                else:
                    continue
        dfs(0,[])
        return ans