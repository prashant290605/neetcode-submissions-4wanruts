from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        hash = defaultdict(list)
        for a,b in edges:
            hash[a].append(b)
            hash[b].append(a)
        
        def dfs(node,parent):
            visited[node] = True

            for i in hash[node]:
                if not visited[i]:
                    dfs(i,node)
        ans = 0   
        for i in range(n):
            if not visited[i]:
                dfs(i,-1)
                ans += 1
        return ans