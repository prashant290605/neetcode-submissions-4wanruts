class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x = nums[0]
        mx_sum = x
        for i in nums[1:]:
            if x < 0:
                x = i
            else:
                x += i
            mx_sum = max(x,mx_sum)
        return mx_sum