class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i:[] for i in range(n)}
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        
        visited = [False]*n
        
        def dfs(node,parent):
            if visited[node]:
                return False
            visited[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        
        x = dfs(0,-1)
        if not x:
            return False
        for i in visited:
            if not i:
                return False
        return True