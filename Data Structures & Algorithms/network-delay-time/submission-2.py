class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u , v , t in times:
            adj[u].append((v,t))
        # dic = {node : float('inf') for node in range(1,n + 1)}

        # for i in range(n-1):
        #     for j in range(1,n+1):
        #         (v,t) = adj[j]
        #         if dic[j] + t <= dic[v]:
        #             dic[v] = dic[j] + t
        # res = max(dic.values())

        # return res if res < float('inf') else -1

# 2nd method
        dist = [float('inf')]*(n)
        dist[k-1] = 0

        # for _ in range(n-1):
        #     for u,v,t in times:
        #         if dist[u-1] + t <= dist[v-1]:
        #             dist[v-1] = dist[u-1] + t
        # res = max(dist)
        # return res if res < float('inf') else -1
        q = deque()
        q.append([k,0])
        while q:
            node , time = q.popleft()
            if time > dist[node-1]:
                continue
            for v,t in adj[node]:
                if dist[node-1] + t < dist[v-1]:
                    dist[v-1] = dist[node-1] + t
                    q.append((v,time + t))
        res = max(dist)
        return res if res < float('inf') else -1
