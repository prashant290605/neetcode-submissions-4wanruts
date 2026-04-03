# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # else:
        #     return False
        
        stack = [(p,q)]
        while stack:
            x,y = stack.pop()
            if not x and not y:
                continue
            if not x or not y or x.val != y.val:
                return False
            else:
                stack.append((x.left,y.left))
                stack.append((x.right,y.right))
        return True