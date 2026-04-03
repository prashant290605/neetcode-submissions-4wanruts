class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(index,prev):
            if index == n:
                return 0
            
            if (index,prev) in memo:
                return memo[(index,prev)]
            
            take = 0
            if prev == -1 or nums[index] > nums[prev]:
                take = 1 + dfs(index+1, index)

            not_take = dfs(index+1,prev)
            memo[(index,prev)] = max(take,not_take)
            return memo[(index,prev)]
            
        return dfs(0,-1)