# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx_sum = float('-inf')
        def dfs(node):
            nonlocal mx_sum
            if not node:
                return 0
            a = dfs(node.left)
            b = dfs(node.right)
            mx_sum = max(mx_sum , node.val + max(0,a) + max(0,b))
            ans = max(node.val + max(a,b),0)
            return ans
        dfs(root)
        return mx_sum