from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visited = [False]*n
        hash = defaultdict(list)
        for i in range(n-1):
            a,b = edges[i]
            hash[a].append(b)
            hash[b].append(a)
        
        def dfs(node,parent):
            if visited[node]:
                return False
            
            visited[node] = True

            for i in hash[node]:
                if i!= parent:
                    if not dfs(i,node):
                        return False
            return True
        
        if not dfs(0,-1):
            return False
        return all(visited)