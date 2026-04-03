from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hash = defaultdict(list)
        for i in range(len(edges)):
            a,b = edges[i]
            hash[a].append(b)
            hash[b].append(a)
        ans = 0
        visited = [False]*n
        def dfs(node,parent):
            if visited[node]:
                return
            visited[node] = True
            for c in hash[node]:
                if c != parent:
                    dfs(c,node)
        
        for i in range(n):
            if not visited[i]:
                dfs(i,-1)
                ans += 1
        return ans