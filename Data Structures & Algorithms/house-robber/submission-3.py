class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = {}
        n = len(nums)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = max(nums[i] + dfs(i+2),dfs(i+1))
        #     return memo[i]
        # return dfs(0)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i],dp[i-1])
        return dp[-1]