# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        self.count = 0
        self.k_th = 0

        def inOrder(node):
            if not node: return None
            inOrder(node.left)
            self.count += 1
            if self.count == k:
                self.k_th = node.val
                return
            inOrder(node.right)
            
        
        inOrder(root)
        return self.k_th