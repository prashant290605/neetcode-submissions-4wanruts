class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u , v , t in times:
            adj[u].append((v,t))
        dic = {node : float('inf') for node in range(1,n + 1)}

        def dfs(node,time):
            if time >= dic[node]:
                return
            
            dic[node] = time
            for v,t in adj[node]:
                dfs(v,t + time)
        
        dfs(k,0)
        res = max(dic.values())
        return res if res < float('inf') else -1