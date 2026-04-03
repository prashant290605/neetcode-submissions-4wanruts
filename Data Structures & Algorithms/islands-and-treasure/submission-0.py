class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        INF = 2**31 - 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        while q:
            row,col = q.popleft()
            for dr,dc in dirs:
                r,c = row+dr,col+dc
                if 0<=r<m and 0<=c<n and grid[r][c] == INF:
                    grid[r][c] = 1 + grid[row][col]
                    q.append([r,c])