class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        mx_left = [0]*n
        mx_left[0] = height[0]
        for i in range(1,n):
            mx_left[i] = max(mx_left[i-1], height[i])
        mx_right = [0]*n
        mx_right[-1] = height[-1]
        for i in range(n-2,-1,-1):
            mx_right[i] = max(mx_right[i+1], height[i])

        ans = 0
        for i in range(n):
            x = min(mx_left[i],mx_right[i]) - height[i]
            if x < 0:
                continue
            else:
                ans += x
        return ans