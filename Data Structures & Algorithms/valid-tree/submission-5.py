from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hash = defaultdict(set)
        for u,v in edges:
            hash[u].add(v)
            hash[v].add(u)
        print(hash)
        visited = [0]*n
        def dfs(node,parent):
            visited[node] = 1

            for nei in hash[node]:
                if nei == parent:
                    continue
                if visited[nei] == 1:
                    return False
                if not dfs(nei,node):
                    return False
            return True
        
        a = dfs(0,-1)
        if not a:
            return False
        for i in visited:
            if not i:
                return False
        return True