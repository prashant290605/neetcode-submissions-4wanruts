# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            x = q.pop()
            a = x.left if x.left else None
            b = x.right if x.right else None
            x.right = a
            x.left = b
            if a:
                q.append(a)
            if b:
                q.append(b)

        return root
