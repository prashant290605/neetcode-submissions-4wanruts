class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        stack.append([0,heights[0]])
        ans = 0
        res = 0
        for i in range(1,len(heights)):
            start = i
            index, height = 0,0
            while stack and heights[i] <= stack[-1][1]:
                index, height = stack.pop()
                res = (i-index) * height
                start = index
                ans = max(res,ans)
            stack.append((start,heights[i]))
            

        while stack:
            index,height = stack.pop()
            res = (len(heights)-index) * height
            ans = max(ans,res)
        return ans