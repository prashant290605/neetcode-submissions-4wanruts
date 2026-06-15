from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = [False]*n
        def dfs(node,parent):
            if visited[node]:
                return 0
            visited[node] = True

            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei,node)
                
            return 1
        for i in range(n):
            if not visited[i]:
                ans += dfs(i,-1)
        return ans