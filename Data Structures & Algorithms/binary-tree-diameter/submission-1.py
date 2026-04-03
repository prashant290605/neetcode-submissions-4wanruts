# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = 0
        # def dfs(node):
        #     nonlocal res
        #     if not node:
        #         return 0
        #     a = dfs(node.left)
        #     b = dfs(node.right)
        #     res = max(res , a+b)
        #     return 1 + max(a,b)
        # dfs(root)
        # return res

        stack = [root]
        mp = {None: (0,0)}

        while stack:
            x = stack[-1]
            if x.left and x.left not in mp:
                stack.append(x.left)
            elif x.right and x.right not in mp:
                stack.append(x.right)
            else:
                x = stack.pop()
                left_height,left_diam = mp[x.left]
                right_height,right_diam = mp[x.right]

                mp[x] = (1+max(left_height,right_height) , max(left_height+right_height,
                left_diam,right_diam))
        return mp[root][1]
