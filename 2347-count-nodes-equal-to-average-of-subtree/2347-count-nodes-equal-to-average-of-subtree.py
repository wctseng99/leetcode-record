# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        output = 0
        
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            node_count = 1 + left[1] + right[1]
            node_sum = node.val + left[0] + right[0]

            nonlocal output
            output += (node.val == node_sum // node_count)

            return (node_sum, node_count)
        
        dfs(root)
        return output