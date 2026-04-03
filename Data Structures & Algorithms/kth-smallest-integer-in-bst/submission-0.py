# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 
        x = 0
        ans = None
        def inorder(node):
            nonlocal x
            nonlocal ans
            if not node:
                return
            if node.left:
                inorder(node.left)
            x += 1
            if x == k:
                ans = node.val
            if node.right:
                inorder(node.right)
            return
        inorder(root)
        return ans