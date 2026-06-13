class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j,val):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == -1:
                return
            
            if grid[i][j] < val:
                return
            else:
                grid[i][j] = val

            dfs(i+1,j,val+1)
            dfs(i,j+1,val+1)
            dfs(i-1,j,val+1)
            dfs(i,j-1,val+1)
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i,j,0)
        