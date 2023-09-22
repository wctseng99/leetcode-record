# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return []
            if node.left is None and node.right is None:
                return [node.val]

            return dfs(node.left) + dfs(node.right)


        return dfs(root1) == dfs(root2)