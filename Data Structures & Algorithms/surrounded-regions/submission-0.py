class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row , col = len(board) , len(board[0])

        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def bfs(rw,cl):
            q = deque([[rw,cl]])

            while q:
                x,y = q.popleft()
                board[x][y] = 'T'
                for r,c in dirs:
                    nr = x+r
                    nc = y+c
                    if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 'O':
                        q.append([nr,nc])
        for r in range(row):
            for c in range(col):
                if r == 0 or r == row-1 or c == 0 or c == col-1:
                    if board[r][c] == 'O':
                        bfs(r,c)
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'