class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        q = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j,0])
        
        while q:
            r,c,t = q.popleft()
            for dr,dc in dirs:
                nr,nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    q.append([nr,nc,t+1])
                    grid[nr][nc] = 0
                ans = t
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

        return ans