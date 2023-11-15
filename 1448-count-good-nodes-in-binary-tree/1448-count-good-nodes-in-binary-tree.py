# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        max_parent = root.val
        res = 0

        def dfs(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                max_val = node.val
                nonlocal res
                res += 1

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, max_parent)
        return res