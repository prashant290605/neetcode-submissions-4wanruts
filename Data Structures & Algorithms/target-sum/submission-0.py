class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        def dfs(index,val):
            if index == n:
                if val == target:
                    return 1
                else:
                    return 0
            
            if (index,val) in memo:
                return memo[(index,val)]

            memo[(index,val)] = dfs(index+1,val-nums[index]) + dfs(index+1,val+nums[index])
            return memo[(index,val)]

        return dfs(0,0) 