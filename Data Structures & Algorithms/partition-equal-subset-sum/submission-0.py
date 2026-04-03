class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        x = 0
        for i in range(n):
            x += nums[i]

        memo = {}
        def dfs(index,val):
            if index == n:
                return False
            
            if (index,val) in memo:
                return memo[(index,val)]

            if val + nums[index] == x/2:
                memo[(index,val)] = True
                return True 

            take = dfs(index+1 , val + nums[index])
            not_take = dfs(index+1 , val)

            memo[(index,val)] = take or not_take
            return memo[(index,val)]

        return dfs(0,0)