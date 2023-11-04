# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        ascend_node = []

        def inOrder(node):
            if not node: return None
            inOrder(node.left)
            ascend_node.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        return ascend_node[k-1]