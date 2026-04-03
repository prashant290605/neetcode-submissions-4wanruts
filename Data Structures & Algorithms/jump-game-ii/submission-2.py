class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        x = 0
        ct = 0
        while x < n-1:
            a = nums[x]
            start = x+1
            end = x+a+1
            if start >= n-1 or end >= n:
                return ct + 1
            mx_reach = 0
            for i in range(start,end):
                if mx_reach < (i + nums[i]):
                    mx_reach = nums[i]
                    x = i
            ct += 1
        return ct