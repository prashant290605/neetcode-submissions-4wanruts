class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        b = [[False]*n for _ in range(n)]
        a = deque()
        for i in range(n):
            for j in range(n):
                if not b[i][j]:
                    a.append([i,j,matrix[i][j]])
                    while a:
                        x,y,val = a.popleft()
                        xnew,ynew = y,n-x-1
                        if not b[xnew][ynew]:
                            a.append([xnew,ynew,matrix[xnew][ynew]])
                        matrix[xnew][ynew] = val
                        b[x][y] = True
        