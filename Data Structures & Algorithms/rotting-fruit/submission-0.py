class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append([r,c,0])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        ans = 0
        while q:
            r,c,x = q.popleft()
            for dr,dc in dirs:
                row,col = r+dr,c+dc
                if 0<=row<m and 0<=col<n and grid[row][col] == 1:
                    q.append([row,col,x+1])
                    grid[row][col] = 0
            ans = x
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        return ans