class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        memo = {}
        def dfs(i,N):
            if i >= N:
                return 0
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(dfs(i+2,N) + nums[i],dfs(i+1,N))
                return memo[i]
        
        x = dfs(0,n-1)
        memo = {}
        y = dfs(1,n)
        return max(x,y)
            