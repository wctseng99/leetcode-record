# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        min_diff, prev = float('inf'), None
        def dfs(node):
            if not node:
                return

            dfs(node.left)

            nonlocal prev
            nonlocal min_diff
            if prev != None:
                min_diff = min(min_diff, abs(prev-node.val))
            prev = node.val

            dfs(node.right)
        
        dfs(root)
        return min_diff