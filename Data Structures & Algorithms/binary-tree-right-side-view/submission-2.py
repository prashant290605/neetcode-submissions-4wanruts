# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # q = deque([root])
        # ans = []
        # while q:
        #     ans.append(q[-1].val)
        #     for i in range(len(q)):
        #         x = q.popleft()
        #         if x.left:
        #             q.append(x.left)
        #         if x.right:
        #             q.append(x.right)
        # return ans
        ans = []
        def dfs(node,depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return ans