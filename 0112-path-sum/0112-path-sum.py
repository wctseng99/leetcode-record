# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, currTarget):
            if not node:
                return False
            
            # leaf node
            if not node.left and not node.right:
                return targetSum == currTarget + node.val
            
            left = dfs(node.left, currTarget + node.val)
            right = dfs(node.right, currTarget + node.val)

            return left or right
        
        return dfs(root, 0)