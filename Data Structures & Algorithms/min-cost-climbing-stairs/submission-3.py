class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # store = {}
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
        #     else:
        #         if i in store:
        #             return store[i]
        #         else:
        #             store[i] = cost[i] + min(dfs(i+1),dfs(i+2))
        #             return store[i]
        # return min(dfs(0),dfs(1))
        n = len(cost)
        # dp = [0]*(n+1)
        # for i in range(2,n+1):
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        # return dp[n]
        one = 0
        two = 0
        for i in range(2,n+1):
            temp = min(one + cost[i-2], two + cost[i-1])
            one = two
            two = temp
        return two