# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return True
        def same(n,m):
            if not n and not m:
                return True
            if n and m and n.val == m.val:
                return same(n.left,m.left) and same(n.right,m.right)
            else:
                return False       
        stack = [root]
        while stack:
            a = stack.pop()
            if a.val == subRoot.val:
                if same(subRoot,a):
                    return True
                
            
            if a.left:
                stack.append(a.left)
            if a.right:
                stack.append(a.right)
        return False