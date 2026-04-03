# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hash = {val : idx for idx,val in enumerate(inorder)}
        # self.pre_idx = 0
        # def dfs(l,r):
        #     if l > r:
        #         return None
        #     root_val = TreeNode(preorder[self.pre_idx])
        #     self.pre_idx += 1
        #     mid = hash[root_val.val]
        #     root_val.left = dfs(l,mid-1)
        #     root_val.right = dfs(mid+1,r)
        #     return root_val
        # return dfs(0,len(inorder)-1)

# weird method
        preidx , inidx = 0,0
        def dfs(limit):
            nonlocal preidx
            nonlocal inidx
            if preidx >= len(preorder):
                return None
            if inorder[inidx] == limit:
                inidx += 1
                return None
            root = TreeNode(preorder[preidx])
            preidx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))
