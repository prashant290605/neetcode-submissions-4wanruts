import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while heap:
            val, i, j = heapq.heappop(heap)
            
            if i == n-1 and j == n-1:
                return val
            
            if visited[i][j]:
                continue
            visited[i][j] = True
            
            for dx, dy in dirs:
                r, c = i + dx, j + dy
                if 0 <= r < n and 0 <= c < n and not visited[r][c]:
                    heapq.heappush(heap, (max(val, grid[r][c]), r, c))