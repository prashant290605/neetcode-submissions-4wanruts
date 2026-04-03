class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def dfs(idx):
            if idx >= n-1:
                return True
            if nums[idx] == 0:
                return False
            if idx in memo:
                return memo[idx]

            for i in range(1,nums[idx]+1):
                if dfs(idx + i):
                    memo[idx] = True
                    return memo[idx]
            memo[idx] = False
            return memo[idx]
        return dfs(0)