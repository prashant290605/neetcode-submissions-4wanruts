# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def dfs(node):
        #     if not node:
        #         return None
        #     if node.val == p.val or node.val == q.val:
        #         return node
        #     a = dfs(node.left)
        #     b = dfs(node.right)
        #     if a and b:
        #         return node
        #     return a or b

        # return dfs(root)
# the above is optimal for binary tree
# below for binary search tree

        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else: 
                return curr