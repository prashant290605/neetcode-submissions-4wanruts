class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        left = height[0]
        right = height[n-1]

        res = 0
        while l < r:
            if left < right:
                l += 1
                left = max(left,height[l])
                if (left-height[l] >= 0):
                    res += left-height[l] 
            else:
                r -= 1
                right = max(right,height[r])
                if (right-height[r] >= 0):
                    res += right-height[r] 
        return res