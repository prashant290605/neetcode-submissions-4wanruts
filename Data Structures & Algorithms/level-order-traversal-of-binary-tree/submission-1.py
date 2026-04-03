# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # q = deque([root])
        # ans = []
        # while q:
        #     a = []
        #     for i in range(len(q)):
        #         x = q.popleft()
        #         if x.left:
        #             q.append(x.left)
        #         if x.right:
        #             q.append(x.right)
        #         a.append(x.val)
        #     ans.append(a)
        # return ans

        # dfs solution below
        res = []
        def dfs(node,depth):
            if not node:
                return 
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return res