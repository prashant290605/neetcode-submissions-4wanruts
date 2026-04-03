# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,mini,maxi):
            if not node:
                return True

            if mini < node.val and maxi > node.val:
                a = dfs(node.left,min(mini,node.val) , min(maxi,node.val))
                b = dfs(node.right , max(mini,node.val) , max(maxi,node.val))
                return a and b
            else:
                return False
        return dfs(root,float('-inf'),float('inf'))