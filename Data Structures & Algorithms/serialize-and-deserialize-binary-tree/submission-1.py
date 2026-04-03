# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # if not root:
        #     return '#'
        # res = []
        # q = deque([root])
        # while q:
        #     x = q.popleft()
        #     if not x:
        #         res.append('#')
        #     else:
        #         res.append(str(x.val))
        #         q.append(x.left)
        #         q.append(x.right)
        # return ','.join(res)
#dfs solution
        res = []
        def dfs(node):
            if not node:
                res.append('#')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        # if vals[0] == '#':
        #     return None
        # root = TreeNode(int(vals[0]))
        # q = deque([root])
        # index = 1
        # while q:
        #     x = q.popleft()
        #     if vals[index] != '#':
        #         x.left = TreeNode(int(vals[index]))
        #         q.append(x.left)
        #     index += 1
        #     if vals[index] != '#':
        #         x.right = TreeNode(int(vals[index]))
        #         q.append(x.right)
        #     index += 1
        # return root
        self.i = 0
        def dfs():
            if vals[self.i] == '#':
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()