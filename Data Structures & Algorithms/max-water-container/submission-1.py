class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        mx = 0
        while l < r:
            water = min(heights[r],heights[l]) * (r-l)
            mx = max(mx,water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mx