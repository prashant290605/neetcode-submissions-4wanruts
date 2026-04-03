class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.idx = -1
        self.ref = 0
    
    def addword(self,word,i):
        cur = self
        cur.ref += 1
        for c in word:
            j = ord(c)-ord('a')
            if cur.children[j] == None:
                cur.children[j] = TrieNode()
            cur = cur.children[j]
            cur.ref += 1
        cur.idx = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row,col = len(board),len(board[0])
        root = TrieNode()
        for i in range(len(words)):
            root.addword(words[i],i)
        
        def getidx(c):
            return ord(c)-ord('a')
        res = []

        def dfs(r,c,node):
            if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == '*' or not node.children[getidx(board[r][c])]):
                return 

            temp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[getidx(temp)]
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.ref -= 1
                if not node.ref:
                    prev.children[getidx(temp)] = None
                    node = None
                    board[r][c] = temp
                    return
            dfs(r-1,c,node)
            dfs(r+1,c,node)
            dfs(r,c-1,node)
            dfs(r,c+1,node)

            board[r][c] = temp

        for r in range(len(board)):
           for c in range(len(board[0])):
                dfs(r,c,root)
        return res

            