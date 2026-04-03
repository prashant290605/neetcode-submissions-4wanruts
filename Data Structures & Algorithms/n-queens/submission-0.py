class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [False]* n
        posdiag = [False] * 2*n
        negdiag = [False] * 2*n
        ans = []
        board = [['.'] * n for i in range(n)]
        def dfs(r):
            if r == n:
                x = [''.join(row) for row in board]
                ans.append(x)
                return
            
            for c in range(n):
                if col[c] or posdiag[r+c] or negdiag[r-c+n]:
                    continue
                col[c] = True
                posdiag[r+c] = True
                negdiag[r-c+n] = True

                board[r][c] = 'Q'
                dfs(r+1)
                col[c] = False
                posdiag[r+c] = False
                negdiag[r-c+n] = False
                board[r][c] = '.'
        dfs(0)
        return ans