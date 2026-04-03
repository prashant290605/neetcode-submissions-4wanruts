# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x = True
        def dfs(node):
            nonlocal x
            if not node:
                return 0
            a = dfs(node.left)
            b = dfs(node.right)
            if (abs(a-b) > 1):
                x = False
            return 1 + max(a,b)
        dfs(root)
        return x
