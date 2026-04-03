class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            else:
                if i in store:
                    return store[i]
                else:
                    store[i] = cost[i] + min(dfs(i+1),dfs(i+2))
                    return store[i]
        return min(dfs(0),dfs(1))