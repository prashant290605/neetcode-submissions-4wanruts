class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water_level = [0]*n #water stored at ith position
        max_left = [1]*n #maximum height on left from current position
        max_left[0] = height[0]
        max_right = [1]*n #maximum height on right from the current position
        max_right[-1] = height[-1]

        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i+1])
        
        for i in range(n):
            water = (min(max_left[i],max_right[i]) - height[i])
            if water >= 0:
                water_level[i] = water
            else:
                water_level[i] = 0

        ans = 0
        for i in water_level:
            ans += i
        return ans