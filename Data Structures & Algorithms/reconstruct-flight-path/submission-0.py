class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src,dst in tickets:
            adj[src].append(dst)
        

        res = ['JFK']
        def dfs(src):
            if len(tickets) + 1 == len(res):
                return True
            if not adj[src]:
                return False
            
            temp = list(adj[src])
            for i,v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                res.pop()
                adj[src].insert(i,v)
        dfs('JFK')
        return res