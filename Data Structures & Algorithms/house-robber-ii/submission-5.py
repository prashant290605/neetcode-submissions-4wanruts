class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        return max(self.helper(nums[:-1]),self.helper(nums[1:]))
    
    def helper(self,nums):
        x = 0
        y = 0
        n = len(nums)
        for i in range(n):
            temp = max(nums[i] + x,y)
            x = y
            y = temp
        return y