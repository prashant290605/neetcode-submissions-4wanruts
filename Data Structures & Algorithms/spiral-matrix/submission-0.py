class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m,n = len(matrix),len(matrix[0])
        left = 0
        right = n-1
        top = 0
        bottom = m-1

        while left <= right and top <= bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans

            
            