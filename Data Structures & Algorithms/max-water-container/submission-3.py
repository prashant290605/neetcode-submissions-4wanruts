class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        r = n-1
        ans = 0
        while l < r:
            vol = min(heights[l],heights[r]) * (r-l)
            ans = max(ans,vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans