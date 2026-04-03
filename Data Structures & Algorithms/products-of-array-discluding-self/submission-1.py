class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        l = 1
        r = 1
        for i in range(1,n):
            l *= nums[i-1]
            left[i]*= l
        for i in range(n-2,-1,-1):
            r *= nums[i+1]
            right[i]*= r
        for i in range(n):
            right[i] *= left[i]
        return right
        