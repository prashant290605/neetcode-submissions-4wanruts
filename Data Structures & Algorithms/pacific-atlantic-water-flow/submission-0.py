class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col = len(heights) , len(heights[0])

        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        pac = [[False]*col for i in range(row)]
        atl = [[False]*col for i in range(row)]
        ans = []

        pacific = []
        atlantic = []
        for i in range(row):
            pacific.append([i,0])
            atlantic.append([i,col-1])
        for i in range(col):
            pacific.append([0,i])
            atlantic.append([row-1,i])
        
        def bfs(source,ocean):
            q = deque(source)
            
            while q:
                x,y = q.popleft()
                ocean[x][y] = True
                for r,c in dirs:
                    if x+r >= 0 and y+c >=0 and x+r < row and y+c < col and not ocean[x+r][y+c] and heights[x+r][y+c] >= heights[x][y]:
                        q.append([x+r,y+c])
                    
        bfs(pacific,pac)
        bfs(atlantic,atl)
        for i in range(row):
            for j in range(col):
                if pac[i][j] and atl[i][j] :
                    ans.append([i,j])
        return ans