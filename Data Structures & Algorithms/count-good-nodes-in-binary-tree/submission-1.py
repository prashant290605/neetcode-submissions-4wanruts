# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        
        # ans = 1
        # def dfs(node,maxval):
        #     nonlocal ans
        #     if not node:
        #         return 
        #     if node.left:
        #         if node.left.val >= maxval:
        #             ans += 1 
        #             dfs(node.left,node.left.val)
        #         else:
        #             dfs(node.left , maxval)
        #     if node.right:
        #         if node.right.val >= maxval:
        #             ans +=1 
        #             dfs(node.right, node.right.val)
        #         else:
        #             dfs(node.right , maxval)
        # dfs(root,root.val)
        # return ans
# below is bfs answer
        q = deque([(root,float('-inf'))])
        res = 0
        while q:
            node,maxval = q.popleft()
            if node.val >= maxval:
                res += 1
            if node.left:
                q.append((node.left,max(maxval, node.val)))
            if node.right:
                q.append((node.right,max(maxval, node.val)))
        return res